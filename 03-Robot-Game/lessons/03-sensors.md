# Lesson 03 — Sensors: Gyro & Color

**Concepts:** what sensors measure, reading live values, using conditions.
Sensors turn "hope" into "know."

## Warm-up (5 min)

Play "robot navigator": one kid blindfold-voice-controls another to a target —
then compare to the same kid walking it with eyes open. Sensors = eyes.

## Teach (10 min)

- **Gyroscope:** measures heading/rotation. Use: `when [heading] = X` or
  `turn to heading`. Caveat: gyro can drift; keep robot still while starting.
- **Color sensor:** reads reflected light / color. Black lines read "dark",
  mat reads "light" — show live values over both.
- **Motor sensors:** every motor knows its position — useful for detecting a
  stalled attachment (pressing against something).

## Hands-on (25 min)

1. Gyro square (from Lesson 02) — now with `turn to heading` blocks only.
2. Color: stop exactly when crossing a black line. Then: wait for line,
   then turn. Precision check with a ruler.
3. Wall squaring: drive backward into the wall for 1 second — robot
   self-aligns square. Run a "drive out, come back, square up, drive out
   again" loop and check the second departure is identical to the first.

## Debrief (5 min)

- Which alignments are free on our field? (walls, lines, mission models)
- Rule of thumb: never rely on pure dead-reckoning for the last 10 cm before
  a mission — line up on something real.

## Success criteria

☐ Gyro square within a few cm
☐ Can stop on a line ±1 cm, 3× in a row
☐ Has used wall-squaring in at least one mission approach
