# Lesson 04 — Line Following

**Concepts:** two-state (zigzag) following with one color sensor; when line
following beats dead reckoning. Many strong teams use it for long, precise
approaches; many others never need it. Teach it, let the team decide.

## Warm-up (5 min)

Ask: "Our robot drifts over a 1.5 m drive. What could correct it
continuously?" Let them generate: walls, lines, landmarks.

## Teach (10 min)

- One-sensor zigzag: if you see the line edge, steer left; else steer right.
  The robot wiggles along the edge. Slow but self-correcting.
- In Word Blocks: a `repeat forever` (or repeat-until) with an
  `if color < threshold → steering −20, else +20` structure.
- Tuning: sensor height (~5–10 mm), speed vs. accuracy trade-off.

## Hands-on (25 min)

1. Follow a straight black line on the mat edge to edge. Time it.
2. Follow a curve. Where does it lose the line? Adjust speed.
3. Combine: dead-reckon most of the distance, line-follow the last stretch
   into a mission, end on a line-stop.

## Debrief (5 min)

- Which missions on our field have usable lines nearby? Check the field map.
- Decide as a team: adopt for specific approaches or skip this season.

## Success criteria

☐ Follows a straight line edge-to-edge without losing it
☐ Team has made an explicit adopt/skip decision with reasons (log it in
  the design decisions log)
