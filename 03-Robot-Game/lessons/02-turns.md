# Lesson 02 — Precise Turns

**Concepts:** pivot vs. spin turns, calculating turn angle from wheel rotations,
introducing the gyro as the accurate alternative.

## Warm-up challenge (5 min)

"Face the robot exactly 90° to the left." Judge by eye — most teams are off
5–10°, and that error compounds down the field.

## Teach (10 min)

- **Spin turn:** both wheels opposite directions — robot pivots in place;
  uses less space. **Pivot turn:** one wheel stopped — arc turn.
- Wheel math: robot spins about its center; each wheel travels
  (turn angle / 360) × robot's turn circumference. It's faster for kids to
  **calibrate empirically**: try X rotations → measure actual angle → scale.
- The compounding problem: 3° error on turn 1 becomes a miss by turn 3.

## Hands-on (25 min)

1. Calibrate a 90° spin turn: guess → measure with protractor phone app → adjust.
2. Drive a square (4 × "straight 40 cm, turn 90°"). End where you started?
3. Introduce gyro: `turn to heading 90` block. Run the square again. Compare.

## Debrief (5 min)

- When is wheel-turning fine? (short runs, re-alignable next step)
- When do you need the gyro? (long approaches, chained turns)

## Success criteria

☐ Square ends within 5 cm of start with gyro turns
☐ Can name one situation for each method
