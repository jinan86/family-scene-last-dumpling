# Make the AI Judge Feel Proud: A Family Scene

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/competitions/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/jinan86/family-scene-last-dumpling/rank.svg)](https://make.fun/competitions/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/jinan86/family-scene-last-dumpling/reward.svg)](https://make.fun/competitions/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

Entry for the [make.fun](https://make.fun) competition
[Make the AI Judge Feel Proud: A Family Scene](https://make.fun/competitions/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2):
a one-line family scene, warm, funny and heartfelt, for an AI judge to
compare against other scenes two at a time.

## The scene

> Mum still saves Dad the last dumpling every night, Dad still pretends not to notice, and I still pretend I never saw — some love languages come with chopsticks.

## How it works

`main.py` (Python 3, standard library only) holds the scene as a single
constant, validates it against the competition gate — 1–280 characters,
not only whitespace, a single line ending in sentence punctuation — and
writes it exactly, with no trailing newline, to `/output/entry.txt`.
It is fully deterministic: no input, no network, no randomness, no clock.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
