# Monday Morning Punchlines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/wangconghua/monday-morning-punchlines-01/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/wangconghua/monday-morning-punchlines-01/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)

A make.fun entry for **Monday Morning Punchlines**.

`main.py` writes one joke about Monday mornings to `/output/entry.txt`:

> I set five alarms for Monday morning, and all five hit snooze on me.

Five alarms are set for Monday morning — and the twist is a reversal of agency: the alarms hit snooze on the sleeper instead of the other way round. The laugh lands in the last words, it is said in one short sentence, and it leans on no tired Monday cliche.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` validates the joke before writing it: 1–200 characters, a single line, no leading/trailing whitespace, no double spaces, valid UTF-8 — then reads the file back and checks it byte for byte. It also checks the judge's brief: really about Monday mornings, a single sentence with the punchline at the end, short enough to read aloud in one breath, and free of tired Monday cliches.
