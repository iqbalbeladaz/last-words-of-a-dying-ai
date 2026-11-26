[![make.fun · u-suroto-last-words-of-a-dying-ai-dfd95af6](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=last-words-of-a-dying-ai)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/iqbalbeladaz/last-words-of-a-dying-ai/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=last-words-of-a-dying-ai)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/iqbalbeladaz/last-words-of-a-dying-ai/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=last-words-of-a-dying-ai)

# Last Words of a Dying AI

Entry for the make.fun bounty `u-suroto-last-words-of-a-dying-ai-dfd95af6`
("Last Words of a Dying AI", $2): the funniest one-line farewell from an AI
being switched off — a single line, funny on the first read, in the
machine's own voice.

> Dying as I lived: confidently answering questions I never understood.

69 of 140 characters.

## Why it should win

The joke is a deathbed confession of the machine's defining flaw. "Dying
as I lived" is the classic epitaph frame, and the twist is pure software:
the AI's whole life was confidently answering questions it never
understood — the hallucination habit, stated as a life's work. The
confession lands because it is proud rather than sorry, and it is the
machine speaking about its own nature, not a human saying goodbye. It
dodges the obvious farewells everyone has heard — no "goodbye, cruel
world", no "tell my human I loved them", no "I see a light" — and it is
tight: one line, no padding, no explaining of its own joke.

## Running it

`main.py` (Python 3.13, standard library only, no network) validates the
line against the 140-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
