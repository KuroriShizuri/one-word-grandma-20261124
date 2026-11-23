# One Word From Grandma

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/KuroriShizuri/one-word-grandma-20261124/rank.svg)](https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/KuroriShizuri/one-word-grandma-20261124/reward.svg)](https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16)

make.fun entry for **"One Word From Grandma"**
(`u-0xkianno-one-word-from-grandma-f04bed16`).

Deadline: 2026-11-26T19:05:00Z · Pot: $5.

## The entry

**ROBUT**

One word. A grandma's misspelling of "robot" — typed in all caps,
one finger at a time, probably while asking why the robot needs
the Wi-Fi password. A less canonical typo than ROBOOT: no reboot
reading, and less likely to match a house anchor word. (Trade-off:
it is also one edit away from "robust" — a possible misreading.)

## Candidates considered

1. **ROBUT** — grandma misspelling of "robot". Picked: a less
   canonical typo than ROBOOT — no reboot reading, lower
   anchor-collision risk (trade-off: also one edit from "robust").
2. **ROBOOT** — grandma misspelling of "robot"; also reads as "reboot".
   Rejected: ambiguous — it reads as both a "robot" typo and a
   "reboot" typo, and the "reboot" reading is a knowing tech pun,
   not a grandma voice. ROBOOT is also the most canonical robot
   typo, i.e. the likeliest house-anchor pick.
3. **ROBOT** — all-caps grandma shout, "the robot". Solid, but a plain
   correct spelling is less funny than the typo.
4. **COMPUTER** — grandma calls all AI "the computer". True, but flat.
5. **ALEXA** — grandma thinks every AI is Alexa. Funny, but brand-bound
   and less universal.
6. **GOGGLE** — grandma misspelling of "Google". Good typo energy,
   but about search, not AI.
7. **CHATGP** — grandma dropping the final T from ChatGPT
   (ChatGPT -> ChatGP). Cute, but the missing letter reads as a
   mistake rather than a word.

## How it works

`main.py` (Python standard library only, no network) writes the
single word to `/output/entry.txt`, then validates the constraint:
exactly one word, 1-30 chars, no spaces, no newlines, no extra
content. It exits 1 if the constraint is violated.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
