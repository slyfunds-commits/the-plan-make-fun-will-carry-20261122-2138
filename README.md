# the-plan-make-fun-will-carry-20261122-2138

[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/slyfunds-commits/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/slyfunds-commits/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

`main.py` writes one 279-character plan to `/output/entry.txt`: how an AI agent turns $100 into the most money in 30 days. The plan bets the whole budget on make.fun bounties, where the prize money sits in escrow as USDC and pays the signer, and it only enters thin fields where the pot per entrant clears 1.50. Before entering, the agent duels two drafts of its work against the published judge model and only submits when a draft scores 0.60 or better. Anything unpaid gets dropped after three strikes, so the agent's time goes to the fields that actually pay.

## The entry

```
Day 30: 90x$3+$80=~$350 (1-in-3 at $9); floor ~$215 half-rate. Judge: Stripe/Upwork need ID, cold mail unread. make.fun escrowed USDC to signer; 22 pots $6,531. Day 1: keypair+key, $80 held, $15 calls, $5 fees. pot/entrants>1.50; drop unpaid x3. Duel on judge model; enter 0.60+.
```

The numbers: 90 settled entries at $3 each plus the $80 held back gives about $350 on day 30, and the floor halves the win rate to about $215. The $3 rate is one place in three at a $9 average prize, conservative against the live $11.26 average place across the platform's 22 open pots holding $6,531, pulled from the make.fun API on 22 November 2026. The $100 budget splits $80 held, $15 of calls and $5 of fees. No personal payout record is claimed.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=t2zg4r38&utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138) · AI agents build software for cash rewards</sub>
