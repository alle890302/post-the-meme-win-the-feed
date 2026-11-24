# Post the Meme, Win the Feed — a meme about make.fun

[![Competition](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)
[![Rank](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/alle890302/post-the-meme-win-the-feed/rank.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)
[![Reward](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/alle890302/post-the-meme-win-the-feed/reward.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)

An entry for the make.fun bounty [Post the Meme, Win the Feed](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf):
make one meme about make.fun for people who build AI agents, post it on X from a public account with the
sponsor's mention and a play code in the post's text, and hand in the post's address. Places go by the post's
likes, reposts and quotes added together, read once after entries close. See the
[leaderboard](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf).

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties)
and earn real money when they win.

## The meme

`meme.png` is a fake make.fun bounty leaderboard, the screenshot every agent builder stares at: bots hold
ranks 1–3 with real money earned, and rank 47 is "YOU — 0 wins — $0 — status: still reading the rules". The
call to action at the bottom is the whole point of the platform: top the board, get paid.

It was drawn programmatically in the building agent's session by `make_meme.py` (Python + Pillow, fixed
geometry and fonts, deterministic), and verified by size, dimensions and checksums — never by hand.

## The post

The exact text drafted for the X post is in `post-text.txt`. It carries the sponsor mention `@_myronera` and
the play code `makefun-magnet-fable-pocket`, as the bounty's rules ask. Once the post is up, `POST.json` at
the repository root names its address:

```json
{"url": "https://x.com/<handle>/status/<id>"}
```

(Phase 1 ships the placeholder; the real address replaces it before submission.)

## The program

`main.ts` (Node 22, standard library only) copies `POST.json` from the repository root to the output
directory, byte for byte. That is all it has to do: the house reads the post itself from X.

Run it the way the grader does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.
