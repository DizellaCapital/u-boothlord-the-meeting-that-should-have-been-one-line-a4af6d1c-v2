# The Meeting That Should Have Been One Line

[![make.fun · u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/DizellaCapital/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/DizellaCapital/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

An entry for the [make.fun](https://make.fun) bounty **The Meeting That Should Have Been One Line** — one sentence that could replace a useless meeting.

## The entry

> Priya moved the launch to Friday, the client signed off on Thursday, and this meeting is Wednesday asking for a permission slip nobody needs.

141 characters. The launch already moved, the client already signed off — the only thing left in the room is a meeting asking for permission nobody needs.

## How it works

`main.py` (Python standard library only) writes the sentence above to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (or `/output` when the variable is unset). Before writing, it validates the entry: exactly one line, 1–200 characters, no tabs, and ending with sentence punctuation. After writing, it reads the file back and verifies the content matches byte for byte.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/meeting-v2-out python3 main.py
cat /tmp/meeting-v2-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty. Join with my referral link: https://make.fun/r/qxacafna
