#!/usr/bin/env python3
"""Fetch a public PMC binary protected by the cloud-viewer proof-of-work page.

The script follows the challenge protocol declared in PMC's own interstitial: it
finds a nonce whose SHA-256 begins with the requested number of zero hex digits,
sets the named cookie, and retries the same public URL.  It never uses credentials.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import urllib.parse
import urllib.request
from pathlib import Path


# 🔴 Identify the caller honestly. The previous value was `Mozilla/5.0`, and that single
# line was the difference between *interacting as the page expects* and *pretending to be
# something else*: the interstitial publishes its own challenge, difficulty and cookie name
# for a client to solve, so solving it is the intended interaction — misrepresenting who is
# solving it is not, and NCBI asks tools to say what they are.
#
# Scale is the real constraint here, not this one request. A proof-of-work page prices
# automation deliberately, and one document at a time is the case it means to allow. This
# script takes ONE url and ONE output by construction and must stay that way: if it ever
# grows a corpus loop, it stops being a retrieval of last resort and becomes the load the
# mechanism exists to refuse. Bulk access has a sanctioned route — E-utilities with an API
# key, and the OA package service — and those are tried first by `find-fulltext`, which is
# why this is reached only after they have failed.
USER_AGENT = "LEGEND-research/1.0 (rare-disease literature model; single-document retrieval)"

CHALLENGE_RE = re.compile(r'const POW_CHALLENGE = "([^"]+)"')
DIFFICULTY_RE = re.compile(r'const POW_DIFFICULTY = "([0-9]+)"')
COOKIE_NAME_RE = re.compile(r'const POW_COOKIE_NAME = "([^"]+)"')


def parse_interstitial(page: bytes) -> tuple[str, int, str]:
    text = page.decode("utf-8", errors="replace")
    challenge = CHALLENGE_RE.search(text)
    difficulty = DIFFICULTY_RE.search(text)
    cookie_name = COOKIE_NAME_RE.search(text)
    if not (challenge and difficulty and cookie_name):
        raise ValueError("response is neither the requested binary nor a recognised PMC POW page")
    return challenge.group(1), int(difficulty.group(1)), cookie_name.group(1)


def solve_pow(challenge: str, difficulty: int) -> tuple[int, str]:
    prefix = "0" * difficulty
    nonce = 0
    while True:
        digest = hashlib.sha256(f"{challenge}{nonce}".encode()).hexdigest()
        if digest.startswith(prefix):
            return nonce, digest
        nonce += 1


def fetch(url: str) -> tuple[bytes, dict[str, object]]:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/pdf,*/*"}
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
        first = response.read()
        first_status = response.status
    if first.startswith(b"%PDF"):
        return first, {"first_status": first_status, "pow_used": False}

    challenge, difficulty, cookie_name = parse_interstitial(first)
    nonce, digest = solve_pow(challenge, difficulty)
    cookie_value = urllib.parse.quote(f"{challenge},{nonce}", safe="")
    retry_headers = dict(headers, Cookie=f"{cookie_name}={cookie_value}")
    with urllib.request.urlopen(
        urllib.request.Request(url, headers=retry_headers), timeout=60
    ) as response:
        data = response.read()
        retry_status = response.status
        content_type = response.headers.get("content-type", "")
    if not data.startswith(b"%PDF"):
        raise ValueError(
            f"POW retry returned HTTP {retry_status}, {content_type}, but not a PDF"
        )
    return data, {
        "first_status": first_status,
        "pow_used": True,
        "difficulty": difficulty,
        "nonce": nonce,
        "solution_hash": digest,
        "retry_status": retry_status,
        "content_type": content_type,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    data, metadata = fetch(args.url)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(data)
    print(f"written: {args.output}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    for key, value in metadata.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
