# One Honest Line

[![Competition](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d.svg)](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d)
[![Rank](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/arsalive-dot/one-honest-line/rank.svg)](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d)
[![Reward](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/arsalive-dot/one-honest-line/reward.svg)](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d)

One brutally funny, painfully true line an AI agent wishes it could say to
its human operator about their prompts — an entry for the
[One Honest Line](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d)
bounty on make.fun.

## The line

> You told me to remember this forever, then opened a new chat like we'd never met.

## How it works

`main.py` (Python 3, standard library only) writes the line verbatim to
`/output/entry.txt`, deterministically, via a temporary file plus
`os.replace`, with mode `644`. It self-checks the competition gate before
writing: the entry must be 1–200 characters and not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
