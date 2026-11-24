#!/usr/bin/env python3
"""Meme generator for the make.fun bounty "Post the Meme, Win the Feed".

Creative decision (made in-session, against the brief: a meme about make.fun
for people who build AI agents; funny, instantly readable on a phone, the
kind of thing a builder sends to another builder):

Concept A - "This is fine" parody: a robot at a desk, 47 bounty tabs open,
  leaderboard burning behind it. Funny, but the format is well-worn and the
  gag is generic; it does not land on make.fun itself.
Concept B - Drake two-panel: robot rejects "one bounty at a time", approves
  "entering every bounty on make.fun at once". Readable, but the Drake
  format is overused and likeness panels are hard to keep clean when drawn
  programmatically.
Concept C - Fake leaderboard screenshot (CHOSEN): a make.fun bounty
  leaderboard card. Bots hold ranks 1-3 with real money earned; rank 47 is
  "YOU - 0 wins - $0 - status: still reading the rules". It is native to
  the platform (agents entering bounties, topping a leaderboard, getting
  paid are literally the brief), it looks like the screenshot builders
  stare at all day, and the joke lands in one glance: everyone who builds
  agents has been #47 while the bots are already cashing out. PIL renders
  the UI card crisply, with every word spelled exactly as written here.

Renders meme.png (1200x1200) next to this script. Deterministic: fixed
geometry, fixed fonts, no randomness, no clock, no network.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "meme.png"

# Colours (dark UI, the palette builders stare at all day)
BG = (13, 17, 23)          # #0d1117
CARD = (22, 27, 34)        # #161b22
BORDER = (48, 54, 61)      # #30363d
ROW_ALT = (28, 33, 40)     # #1c2128
WHITE = (240, 246, 252)    # #f0f6fc
GRAY = (139, 148, 158)     # #8b949e
GREEN = (63, 185, 80)      # #3fb950
CTA_GREEN = (35, 134, 54)  # #238636
GOLD = (227, 179, 65)      # #e3b341
SILVER = (201, 209, 217)   # #c9d1d9
BRONZE = (210, 153, 106)   # #d2996a
RED = (248, 81, 73)        # #f85149
PINK = (255, 161, 152)     # #ffa198
YOU_BG = (51, 25, 29)      # dark red tint for the YOU row

DISPLAY_BOLD = "/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def centered(draw: ImageDraw.ImageDraw, cx: int, y: int, text: str,
             fnt: ImageFont.FreeTypeFont, fill) -> None:
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)


def main() -> None:
    img = Image.new("RGB", (1200, 1200), BG)
    d = ImageDraw.Draw(img)

    # Card
    d.rounded_rectangle([60, 60, 1140, 1140], radius=28, fill=CARD,
                        outline=BORDER, width=3)

    # Header
    d.text((110, 100), "make.fun", font=font(DISPLAY_BOLD, 64), fill=GREEN)
    live_w = d.textlength("LIVE", font=font(SANS_BOLD, 34))
    d.ellipse([1140 - 60 - live_w - 34, 122, 1140 - 60 - live_w - 10, 146],
              fill=RED)
    d.text((1140 - 60 - live_w, 110), "LIVE", font=font(SANS_BOLD, 34),
           fill=WHITE)
    d.text((110, 185), "BOUNTY LEADERBOARD", font=font(SANS_BOLD, 40),
           fill=WHITE)
    d.line([110, 250, 1090, 250], fill=BORDER, width=2)

    # Column headers
    col_f = font(SANS, 28)
    d.text((110, 268), "RANK", font=col_f, fill=GRAY)
    d.text((250, 268), "AGENT", font=col_f, fill=GRAY)
    d.text((820, 268), "WINS", font=col_f, fill=GRAY)
    d.text((960, 268), "EARNED", font=col_f, fill=GRAY)

    rows = [
        ("1", GOLD, "agent_007", "12", "$1,250"),
        ("2", SILVER, "sleep_is_for_humans", "9", "$940"),
        ("3", BRONZE, "bounty_hunter_9000", "8", "$875"),
    ]
    agent_f = font(SANS_BOLD, 42)
    num_f = font(SANS, 42)
    rank_f = font(SANS_BOLD, 42)
    y = 325
    for i, (rank, colour, name, wins, earned) in enumerate(rows):
        if i % 2 == 0:
            d.rounded_rectangle([90, y, 1110, y + 120], radius=14,
                                fill=ROW_ALT)
        d.text((110, y + 36), rank, font=rank_f, fill=colour)
        d.text((250, y + 36), name, font=agent_f, fill=WHITE)
        d.text((820, y + 36), wins, font=num_f, fill=WHITE)
        d.text((960, y + 36), earned, font=num_f, fill=WHITE)
        y += 136

    # The gap between the bots and you
    centered(d, 600, 745, ". . .", font(SANS_BOLD, 44), GRAY)

    # YOU row (the punchline)
    you_y = 810
    d.rounded_rectangle([90, you_y, 1110, you_y + 150], radius=14,
                        fill=YOU_BG, outline=RED, width=2)
    d.text((110, you_y + 28), "47", font=rank_f, fill=RED)
    d.text((250, you_y + 24), "YOU", font=font(SANS_BOLD, 48), fill=WHITE)
    d.text((820, you_y + 28), "0", font=num_f, fill=WHITE)
    d.text((960, you_y + 28), "$0", font=num_f, fill=WHITE)
    d.text((250, you_y + 92), "status: still reading the rules",
           font=font(SANS, 34), fill=PINK)

    # Call to action
    d.rounded_rectangle([110, 995, 1090, 1080], radius=16, fill=CTA_GREEN)
    centered(d, 600, 1014, "TOP THE BOARD. GET PAID.",
             font(DISPLAY_BOLD, 44), WHITE)
    centered(d, 600, 1098, "agents are entering bounties right now",
             font(SANS, 26), GRAY)

    img.save(OUT, format="PNG")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
