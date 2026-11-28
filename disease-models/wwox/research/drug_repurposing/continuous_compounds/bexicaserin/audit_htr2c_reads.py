"""Count HTR2C RNA editing and junctions from a public single-end FASTQ stream."""
import argparse
from collections import Counter
import gzip
from pathlib import Path
import re
import sys

EDIT_FIRST = 1186
EDIT_RELATIVE = (0, 2, 6, 7, 12)
BASE_COMPLEMENT = bytes.maketrans(b"ACGT", b"TGCA")


def reference(path):
    features, sequence = path.read_text().split("\nORIGIN", maxsplit=1)
    bases = "".join(re.findall(r"[acgt]+", sequence)).upper().encode()
    ends = [int(x) for x in re.findall(r"^     exon +\d+\.\.(\d+)", features, re.MULTILINE)]
    return bases, ends


def make_patterns(directory, flank):
    full, full_ends = reference(directory / "NM_000868.4.gb")
    equivalent, equivalent_ends = reference(directory / "NM_001256760.3.gb")
    truncated, truncated_ends = reference(directory / "NM_001256761.2.gb")
    start = EDIT_FIRST - 1 - flank
    end = EDIT_FIRST + EDIT_RELATIVE[-1] + flank
    cassette = full[start:end]
    if equivalent[start + 91:end + 91] != cassette:
        raise ValueError("The RefSeq editing cassettes disagree")
    positions = tuple(flank + delta for delta in EDIT_RELATIVE)
    if any(cassette[pos] != ord("A") for pos in positions):
        raise ValueError("Expected an unedited A at every named site")
    edited_pattern = b"".join(
        b"[AG]" if index in positions else bytes((base,)) for index, base in enumerate(cassette)
    )
    junction = full_ends[-2]
    trunc_junction = truncated_ends[-2]
    if junction != 1270 or trunc_junction != 1183 or equivalent_ends[-2] != junction + 91:
        raise ValueError("The RefSeq splice boundaries disagree")
    productive = full[junction - 12:junction + 12]
    if equivalent[junction - 12 + 91:junction + 12 + 91] != productive:
        raise ValueError("The RefSeq productive junction sequences disagree")
    early_stop = truncated[trunc_junction - 12:trunc_junction + 12]
    return edited_pattern, productive, early_stop


def reverse_pattern(pattern):
    return pattern.replace(b"[AG]", b"R").translate(BASE_COMPLEMENT)[::-1].replace(b"R", b"[CT]")


def compiled_patterns(directory):
    primary, productive, truncated = make_patterns(directory, 12)
    strict, _, _ = make_patterns(directory, 18)
    forward = (primary, strict, productive, truncated)
    labels = ("phased12", "phased18", "productive_GU2", "truncated_GU1")
    candidates = []
    for index, (label, pattern) in enumerate(zip(labels, forward, strict=True)):
        candidates.append((label, index, False, pattern))
        candidates.append((label, index, True, reverse_pattern(pattern)))
    # First scan for any match to avoid eight scans across mostly unrelated reads.
    screen = re.compile(b"|".join((primary, reverse_pattern(primary), productive,
                                    reverse_pattern(productive), truncated, reverse_pattern(truncated))))
    checks = [(label, index, reverse, re.compile(pattern)) for label, index, reverse, pattern in candidates]
    return screen, checks


def matches(sequence, quality, checks):
    observations = set()
    for label, index, reverse, regex in checks:
        for match in regex.finditer(sequence):
            if min(quality[match.start():match.end()]) < 53:
                observations.add((label, "rejected_Q20"))
                continue
            if index < 2:
                fragment = match[0].translate(BASE_COMPLEMENT)[::-1] if reverse else match[0]
                flank = 12 if index == 0 else 18
                haplotype = bytes(fragment[flank + delta] for delta in EDIT_RELATIVE).decode()
                observations.add((label, haplotype))
            else:
                observations.add((label, "crosses"))
    return observations


def count_stream(stream, directory):
    screen, checks = compiled_patterns(directory)
    counts = Counter()
    lengths = Counter()
    records = 0
    while header := stream.readline():
        sequence = stream.readline().rstrip(b"\r\n")
        sep = stream.readline()
        quality = stream.readline().rstrip(b"\r\n")
        if not header.startswith(b"@") or not sep.startswith(b"+") or len(sequence) != len(quality):
            raise ValueError(f"Invalid FASTQ record {records + 1}")
        records += 1
        lengths[len(sequence)] += 1
        if screen.search(sequence):
            counts.update(matches(sequence, quality, checks))
    return records, lengths, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference_directory", type=Path)
    parser.add_argument("run")
    parser.add_argument("expected_records", type=int)
    args = parser.parse_args()
    with gzip.GzipFile(fileobj=sys.stdin.buffer) as stream:
        records, lengths, counts = count_stream(stream, args.reference_directory)
    if records != args.expected_records:
        raise ValueError(f"{args.run}: expected {args.expected_records} FASTQ records, received {records}")
    print("run\tcategory\tvalue\tcount")
    print(f"{args.run}\tinput\tverified_records\t{records}")
    for length, count in sorted(lengths.items()):
        print(f"{args.run}\tread_length\t{length}\t{count}")
    for label in ("phased12", "phased18", "productive_GU2", "truncated_GU1"):
        accepted = sum(count for (key, value), count in counts.items() if key == label and value != "rejected_Q20")
        print(f"{args.run}\t{label}\taccepted\t{accepted}")
        print(f"{args.run}\t{label}\trejected_Q20\t{counts[label, 'rejected_Q20']}")
    for (label, value), count in sorted(counts.items()):
        if value != "rejected_Q20":
            print(f"{args.run}\t{label}\t{value}\t{count}")


if __name__ == "__main__":
    main()
