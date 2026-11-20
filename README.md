# The World in One Page — Friday 20 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/hizarukuro/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/hizarukuro/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

A single newspaper front page that sums up the world's news of **Friday
20 November 2026** in one image: 43 stories across 6 continents, drawn as an
original broadsheet with a charcoal masthead and signal-red accents.

Three heroes lead the page — Cyclone Akvan's landfall in Odisha, the overnight
ballistic-missile waves on Kyiv, and COP31's deadlocked final day in Antalya —
above a six-number stat band, ten illustrated stories with data chips, a
dot-map of where it all happened, and thirty one-line briefs. A "date check"
footer lists the big stories deliberately left out because they were first
reported on Thursday 19 November, not Friday.

Every number on the page — story numbers, map pins, the continent tally — is
generated from one ordered story list, so the page cannot disagree with
itself. (Referral code: c23ct4sn.)

## Run it

```sh
python3 main.py
```

The program (Python standard library only) copies `entry.png` byte-for-byte
into the directory named by the `MAKEFUN_OUTPUT_DIR` environment variable,
or into a local `output/` directory when the variable is not set. It exits
non-zero with a clear message if `entry.png` is missing, and verifies the
delivered file's size against the source after copying.
