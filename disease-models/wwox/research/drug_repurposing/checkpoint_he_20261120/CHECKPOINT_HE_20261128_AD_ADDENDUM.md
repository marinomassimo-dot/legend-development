# Addendum to checkpoint HE-AD (2026-11-28, about 09:35Z): the sampled push, and one correction

- Published: the `--shared` suite clone is on `main` (1792bd8f3760, gate PASS). Section 3 item 1 is closed and the mandate
  step is DONE. Section 3 item 3 is done by the sample below.
- Sample (folder sizes every 3 s through that push, which waited 211 s behind two others): its suite clone peaked at
  **471 MB** (`.git` 4 MB); a suite clone of a publisher ahead, still on the old code, peaked at **1294 MB** (`.git`
  827 MB). Each regeneration used a candidate tree of 470 MB for about 19 s. Suite clone time 2 s.
- **Correction to section 2:** the publication gate wrote no temporary clone. `safe_push` runs it in its default mode;
  the archive-and-extract path runs only in `release` and `clone` modes. The 434 MiB tar and 458 MiB extraction written
  there as part of a push are not part of it, and the "second candidate" (streaming the archive) saves nothing on a push.
- Open for ADV, not changed: the 2 GB floor (`MIN_FREE_GB`) was set at twice a 0.86 GB peak. With a peak near 0.47 GB
  the same rule gives about 1 GB. The lab's standing disk rule also says 2.0 GB, so both would move together.
