#!/usr/bin/env python3
"""Print the thirty-day plan for turning $100 into the most money."""

SEGMENTS = [
    "Stripe/Upwork dead: ID blocks pay, cold mail unread.",
    "make.fun: 22 escrowed pots, $6,531.",
    "Day 1: keypair+key, hold $80, $15 calls, $5 fees.",
    "Enter pot/entrants>1.50 only; quit after 3 unpaid.",
    "Duel on judge model; ship 0.60+.",
    "90x$3+$80=$350, 1-in-3 at $9.",
    "Half rate: $135+$80=$215.",
]


LIMIT = 280


def assemble(parts):
    text = " ".join(parts)
    if len(text) > LIMIT or not text.isascii():
        raise SystemExit("plan breaks the 280-code-point ASCII limit")
    return text


def main():
    print(assemble(SEGMENTS))


if __name__ == "__main__":
    main()
