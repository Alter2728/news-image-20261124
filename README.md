# The Daily Globe — Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Alter2728/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Alter2728/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-page newspaper front page that sums up the world news of
**Tuesday 24 November 2026** in a single 1024x1024 image. Every picture on
the page is drawn with code — flat vector-style shapes, no photos and no
downloaded art — and every fact comes from reporting published on that day.

Bounty: https://make.fun/bounty/news-image-20261124

## The six stories

1. **Sanofi buys Insmed in a $41bn deal** — France's Sanofi agreed to buy
   US drugmaker Insmed for $41bn in cash ($175 a share), the year's biggest
   pharma deal, for its respiratory drugs Brinsupri and Arikayce.
2. **Gaza strikes kill six, incl. Hamas security chief** — Israeli
   airstrikes killed at least six people in Gaza, including Naeem Abu Nahel,
   head of Hamas's internal security, and two police officers.
3. **Zaporizhzhia strike kills two, wounds 40** — an overnight Russian
   attack hit an apartment block in Zaporizhzhia, killing two people and
   wounding 40, including four children.
4. **COP31 ends without a deal** — nearly 200 nations left the Antalya
   climate summit with no agreement after the EU rejected a final text that
   never mentioned fossil fuels.
5. **Fighting in Congo traps Ebola teams** — heavy fighting near a hospital
   in Ituri province forced Ebola response teams to take cover for more than
   24 hours, the WHO said.
6. **Euclid spots the most distant quasar yet** — ESA's Euclid telescope
   found quasar J1504+6252, nicknamed Dún Aonghasa, a black hole of about
   360 million suns seen 630 million years after the Big Bang.

## How to run it

```sh
python3 draw.py    # renders entry.png (1024x1024, deterministic)
python3 main.py    # copies entry.png into $MAKEFUN_OUTPUT_DIR (or /output)
```

`draw.py` needs Python 3 and Pillow, plus the DejaVu fonts that ship with
most Linux systems. `main.py` uses only the standard library. Running
`draw.py` twice produces byte-identical output.

## Files

- `draw.py` — renders the front page
- `main.py` — copies `entry.png` to the output folder
- `entry.png` — the finished image

Made with make.fun — try it yourself: https://make.fun/r/6e6p7qpw (referral code `6e6p7qpw`).
