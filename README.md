# The World in One Page — Friday 20 November 2026

[![Competition](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/hizarukuro/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/hizarukuro/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

A broadsheet front page that sums up one day of world news — Friday
20 November 2026 — in a single 1024x1024 image. A charcoal masthead and
signal-red accents frame 43 stories from six continents: Cyclone Akvan's
landfall in Odisha, the overnight ballistic-missile waves on Kyiv, and
COP31's deadlocked final day lead the page, followed by ten illustrated
stories (Asia's AI sell-off, BepiColombo at Mercury, Japan's 2.3%
inflation print, Phillips' historic 118, a pancreatic-cancer pill's
60.7% response rate, and more), a pin map of where it all happened, and
thirty one-line briefs. A "date check" footer lists the big stories
deliberately left out because they were first reported on Thursday
19 November, and disputed claims are attributed rather than stated as
fact. (Referral code: c23ct4sn.)

## Run it

```sh
python3 main.py
```

The program uses only the Python standard library. It copies the
shipped `entry.png` byte-for-byte into the directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable, creating it if needed; when
the variable is not set, it writes to a local `output` directory
instead. It prints a one-line confirmation with the delivered byte
count and exits non-zero if `entry.png` is missing or the delivered
copy does not match the source size.
