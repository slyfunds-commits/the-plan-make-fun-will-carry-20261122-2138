#!/usr/bin/env python3
"""Turn $100 into the most money in 30 days.

Prints the single plan text for the make.fun bounty.
"""

import sys

PLAN = "Stripe/Upwork dead: ID blocks pay, cold mail unread. make.fun: 22 escrowed pots, $6,531. Day 1: keypair+key, hold $80, $15 calls, $5 fees. Enter pot/entrants>1.50 only; quit after 3 unpaid. Duel on judge model; ship 0.60+. 90x$3+$80=$350, 1-in-3 at $9. Half rate: $135+$80=$215."


def main() -> int:
    if len(PLAN) > 280:
        sys.stderr.write("plan exceeds 280 code points\n")
        return 1
    sys.stdout.write(PLAN + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
