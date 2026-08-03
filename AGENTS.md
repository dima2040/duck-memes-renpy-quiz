# Project Operating Rules

This project is developed as a Ren'Py game intended for a production release on Steam and as an Android APK.

## Collaboration Model

- Keep this thread focused on project planning, roadmap shaping, backlog grooming, and game design discussion.
- Treat the user as the game designer and discuss design questions at that level: goals, player fantasy, pacing, systems, progression, content structure, feedback loops, and release scope.
- Use an incremental, Karpathy-style workflow: make small playable changes, let the user validate them by playing, then decide the next step.
- Do not batch large speculative changes without a playable checkpoint.

## Game Design Direction

- The primary mechanic is a quiz.
- Visual-novel scenes should be short connective tissue between quiz segments: setup, character reactions, consequences, escalation, and payoff.
- The game direction is a broader absurd school meme-comedy, not a pure visual novel.
- The player has no explicit avatar.
- The central meme expert is `МужикБыкКорова`.
- `МужикБыкКорова` is a character/authority figure, not the player avatar unless the game designer explicitly changes that.
- Codex may suggest meme ideas, but all meme canon requires explicit approval from the game designer.
- The game designer provides the main body of memes.

## Sprint And Task Tracking

- Store sprint plans, backlog items, and major tasks in GitHub Issues.
- Prefer one GitHub Issue per coherent sprint, feature, bug, or release task.
- Large issues should include:
  - player-facing goal;
  - implementation scope;
  - validation steps for the user;
  - release/platform impact when relevant;
  - clear done criteria.
- Keep issue titles practical and scannable, for example: `Sprint 0: Playable Ren'Py Foundation`.

## Thread Workflow

- Implement every new sprint or large task in a separate Codex thread.
- When a sprint or large task starts, run it in goal mode with a concrete objective.
- Commit each ready implementation checkpoint before moving to the next sprint or major task, unless the user explicitly asks to keep changes uncommitted.
- Keep commits scoped to one ready step or sprint.
- The planning thread should not become the implementation thread unless the user explicitly says so.
- When the user asks to launch/open/test the latest version, use the canonical `main` checkout and run `tools/launch_latest.cmd` unless the user explicitly requests a specific task worktree or branch.
- Do not silently fast-forward, rebase, or reset old implementation worktrees just to make them "latest"; create new implementation threads from the latest `main` after ready checkpoints are merged and pushed.
- Each implementation thread should:
  - read the relevant GitHub Issue before changing files;
  - keep edits scoped to that issue;
  - produce a playable/testable build or checkpoint when feasible;
  - report what changed and how the user should validate it in-game;
  - leave follow-up ideas as GitHub Issues instead of silently expanding scope.

## Validation Loop

- The user validates game changes primarily by playing the game.
- After each playable checkpoint, wait for user feedback before moving to the next sprint or major task.
- Treat user playtest feedback as design input, not merely bug reports.
- If a change affects Steam or Android release readiness, include platform-specific validation notes.

## Current Roadmap Direction

1. Sprint 0: make the project a clean, launchable Ren'Py project with placeholder assets and basic configuration.
2. Sprint 1: create a small but polished playable vertical slice.
3. Sprint 2: make content easier to expand through better data and scene structure.
4. Sprint 3: add final art, sound, identity, and presentation.
5. Sprint 4: production cleanup and release hardening.
6. Sprint 5: Android APK build pipeline and device validation.
7. Sprint 6: Steam store, SteamPipe build, review, and launch preparation.
8. Sprint 7: release candidate, final QA, versioning, and launch artifacts.
