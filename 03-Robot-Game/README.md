# Robot Game

Everything about the robot: mission analysis, strategy, design evolution, and
code history. The team's rule: **if it isn't documented, we can't explain it
to the judges.**

## Files

| File | Purpose |
|---|---|
| [mission-analysis.md](mission-analysis.md) | Every mission: what, points, difficulty, status |
| [run-strategy.md](run-strategy.md) | Run-by-run plan with expected + actual scores |
| [robot-design-evolution.md](robot-design-evolution.md) | Photo log of every major design change and why |
| [code-log.md](code-log.md) | Version history of programs |
| [lessons/](lessons/) | Skill ladder: driving, sensors, attachments, programming patterns |

## Workflow each meeting

1. Pick a mission from the analysis sheet (or a skill from [lessons/](lessons/)).
2. Plan the run on paper first (start → moves → action → end).
3. Program, test, measure — log the result (success rate out of 5 tries).
4. Save code as a new version; screenshot it into the code log.
5. Update mission status: 💡 idea / 🛠️ building / 🟡 works sometimes / ✅ reliable

## Where good designs come from (steal like a team)

Start from a proven one-kit base robot rather than inventing — FLL Tutorials
hosts builds like **DroidBot 3M, Educator++, Coop Bot**
(flltutorials.com → Robot Game → Building). Priorities for any base: rigid
frame, low center of gravity, color sensors mounted low and shielded from
ambient light, gyro away from motor vibration, and a quick-swap attachment
mount on the front. Then the team's own iteration story happens *on top* of
that starting point — which is exactly what judges want to hear about.

## Free deep-dive lessons to pull when stuck

- Navigation series (8 decks): finding/aligning on lines, wall following,
  launch alignment — flltutorials.com/en/RobotGame.html
- Passive attachments, gyro positioning, sensor shielding, cable management
- PrimeLessons Units 9–10: squaring, proportional line following, reliability

## Reliability standard

A mission counts as **✅ reliable** only after **5 consecutive successful runs**
on the practice table. Track success rates in [run-strategy.md](run-strategy.md) —
the tournament takes your *best* of three rounds, but your score depends on
your *typical* run, so chase consistency first, points second.
