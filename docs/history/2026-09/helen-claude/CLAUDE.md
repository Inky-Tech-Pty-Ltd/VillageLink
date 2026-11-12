# CLAUDE.md — VillageLink staging conventions

This repo uses a two-lane authorship protocol for changes made by "Helen"
(Claude, via Claude Code cloud sessions). Full detail:
reference/helen-claude-github-access-and-authorship.md.

## The one rule that matters here

You (Claude Code, in this repo) are the STAGING side only.

- Stage completed work on `helen-staging/pr/<short-name>` (default) or
  `helen-staging/direct/<short-name>` (only if the person explicitly says
  "express lane").
- Base every staging branch on current `main`.
- NEVER create `helen/*` branches yourself — that namespace belongs to
  the `helen-publish.yml` attribution workflow, triggered separately by
  a `/helen-publish helen-staging/...` comment on the publication control
  issue.
- NEVER open the final review-lane PR yourself. The workflow opens it,
  authored as `Helen-Claude[bot]`.
- After pushing the staging branch, STOP and tell the person the exact
  branch name that's ready — don't go further on your own.

## Publication control

- Issue: #44
- Trigger comment: `/helen-publish helen-staging/pr/<short-name>` (or
  `/helen-publish helen-staging/direct/<short-name>` for express lane)

## If asked to bootstrap or repair the publish plumbing itself

(.github/workflows/helen-publish.yml, the control issue, secrets) — that
work is an exception: it's fine to push it as an ordinary commit, since
it's infrastructure, not "Helen-authored substantive work."

For anything else about the protocol's reasoning or the parallel Puck
setup, see reference/helen-claude-github-access-and-authorship.md and
reference/puck-github-access-and-authorship.md in this repo.
