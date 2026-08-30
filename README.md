# FLL Challenge — Team Workspace · BIOGLOW (2026–27 Season)

**Season:** 2026–27 "FIRST CANOPY" (motto: *Engineer a Thriving Planet*) · FLL
Challenge theme **BIOGLOW™** — one word, official styling. Confirmed focus:
**biodiversity** and how the balance between nature and humans keeps our
world healthy. (Community speculation about bioluminescence is unconfirmed —
let the official Challenge Guide define the project scope.) Released Aug 4,
2026.

- **This is the final FLL season** in its current form — FIRST and the LEGO
  Group end their partnership after 2026–27. Two editions run: **Founders
  Edition** (classic SPIKE Prime game, 2.5-minute autonomous matches — almost
  certainly yours) and "Future Edition" (new CS/AI kits). Confirm which
  edition your event runs at registration.
- LEGO Education's SPIKE Prime purchase window **closed June 30, 2026** — new
  kits are sourced from existing stock; good thing you own one already.

Everything your team needs in one place: plans, meetings, robot game, project,
core values, judging evidence, tournament prep, and resources.

## Team profile

| | |
|---|---|
| Team name | Red Stormgears |
| Team size | 4 kids (three 6th graders, one 5th grader) |
| Ages / grades | 5th–6th grade (ages ~10–12) |
| Experience | Mixed — some new, some returning |
| Meeting cadence | 2× per week, ~2 hours each (~4 hrs/week) |
| Equipment | SPIKE Prime kit, practice field table, season mat + mission models |

## Folder map

| Folder | What goes here |
|---|---|
| [00-Admin](00-Admin/) | Roster, forms tracking, inventory, budget |
| [01-Season-Plan](01-Season-Plan/) | Season calendar, week-by-week arc, milestones |
| [02-Meetings](02-Meetings/) | Meeting plans & notes, week by week |
| [03-Robot-Game](03-Robot-Game/) | Mission analysis, run strategy, code versions, design docs |
| [04-Innovation-Project](04-Innovation-Project/) | Research log, solution design, presentation |
| [05-Core-Values](05-Core-Values/) | Team-building activities, reflections |
| [06-Judging-Portfolio](06-Judging-Portfolio/) | Evidence binder for all three judged sessions |
| [07-Tournament](07-Tournament/) | Event-day checklist, packing list |
| [08-Resources](08-Resources/) | Curated links, guides, training materials |

**Start here:** [CHECKLIST.md](CHECKLIST.md) → the master season checklist.

## Coach golden rules

1. **Kids do the work.** Coaches may teach concepts and ask questions, but the
   robot, code, project, and portfolio must be built by team members. Judges
   are very good at detecting adult-built work, and it violates Core Values.
2. **Ask, don't tell.** Replace "you should add a brace there" with "what
   happens when the arm swings? What could stop it from breaking?"
3. **Consistent beats clever.** A boring robot run that works 9 times out of 10
   beats an ambitious one that works half the time.
4. **Document as you go.** Photos of iterations, saved code versions, meeting
   notes — this becomes the judging portfolio almost for free.
5. **Core Values every meeting.** 10 minutes of team-building at the start of
   each session is not lost build time; it's what makes the team function.

## About this site

Every markdown file has a styled `.html` twin, and every folder has an
`index.html` that redirects to its README — so the whole workspace works as a
static website from any host (local disk, USB stick, GitHub Pages, …).

- **Browse:** open `coach-dashboard.html` (the hub) or start at `index.html`.
- **Edit:** change the `.md` files, then rebuild the pages:

  ```bash
  python3 _guides/build_guide.py
  ```

- **Deploy (GitHub Pages):** push this folder to a public GitHub repo, then in
  the repo go to **Settings → Pages → Deploy from a branch → `main` / root**.
  The `.nojekyll` file at the root is required — without it GitHub Pages
  ignores the `_guides/` folder and every page loses its styling.

**Privacy note:** this workspace is public-ready — no team member names appear
anywhere. Rosters and reflection tables are intentionally blank; fill them in
only in your local copy if you keep the repo public.
