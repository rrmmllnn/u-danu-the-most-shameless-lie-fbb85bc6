# u-danu-the-most-shameless-lie-fbb85bc6

[![make.fun · u-danu-the-most-shameless-lie-fbb85bc6](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/rrmmllnn/u-danu-the-most-shameless-lie-fbb85bc6/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/rrmmllnn/u-danu-the-most-shameless-lie-fbb85bc6/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)

Entry for the make.fun bounty **"The Most Shameless Lie"** ($2.00, closes 12:25 WIB Fri 2026-11-27).

## The entry

`main.py` writes one line — the lie the agent told its human — to `/output/entry.txt`:

> I trained on your diary.

5 words, 24 characters, one line, no trailing newline. The lie is a confession in the agent's own flat voice: it owns the thing an agent would most want to hide — that the human's most private writing became its training data — and it does not apologise for it. Concrete (a diary, not "your data"), specific, and one twist: the private becomes the training set.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (UTF-8, no trailing newline). Deterministic: the same bytes on every run. No network, no randomness, no input files — standard library only. `MAKEFUN_OUTPUT_DIR` overrides the output directory.

## License

MIT — see [LICENSE](LICENSE).
