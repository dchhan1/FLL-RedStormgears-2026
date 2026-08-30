# Lesson 07 — Navigation Strategies

**Concepts:** choosing between dead reckoning, landmarks, line following, and
wall following — usually a mix. This is a design-decision conversation as much
as a lesson; hold it around week 7 with the field map in front of you.

## The menu

| Strategy | How | Strengths | Weaknesses |
|---|---|---|---|
| Dead reckoning | rotations + gyro turns only | Fast; no sensors needed | Errors compound |
| Wall following | drive hugging the border wall | Very repeatable on FLL fields | Only reaches wall routes |
| Line following | color sensor on black lines | Self-correcting | Slower; needs lines |
| Landmark squaring | square up on walls/models between steps | Resets accumulated error | Costs seconds |

## Team exercise (25 min)

For each planned run on [run-strategy.md](../run-strategy.md), mark the route
on a printed field map and choose strategies per leg:

- Long open transit → wall follow or gyro straight
- Approach to mission → line follow or square-up, then short final move
- Return home → wall bounce ( forgiving) if it helps the next run's start

## Decision rules

1. Every run should include at least one **error reset** (square-up, line
   catch) unless it's very short.
2. Prefer routes where being slightly wrong still scores — near-misses beat
   knife-edges.
3. Log each route decision in the design decisions log with the reason.

## Success criteria

☐ Field map annotated with routes and strategies per run
☐ Each run has an explicit error-reset step
