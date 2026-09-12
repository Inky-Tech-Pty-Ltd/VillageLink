# Puck-GPT GitHub attribution

Village Link uses two legitimate contribution lanes for Puck-GPT.

## Direct lane

Use this for changes that do not need Joe Rasmussen's review before they land.

Expected GitHub history:

- Puck-GPT authors the change.
- Puck-GPT commits directly to `main`.

## Review lane

Use this when Joe should inspect, test, or explicitly accept the change before integration.

Expected GitHub history:

- Puck-GPT authors the change on a Puck branch.
- Puck-GPT opens the pull request.
- Joe Rasmussen reviews and/or acceptance-tests it.
- Joe Rasmussen merges it into `main`.

The goal is not to force every change through the same ceremony. The goal is for GitHub to record who actually did what.

## ChatGPT bridge

The ordinary ChatGPT GitHub connector acts through Joe Rasmussen's authenticated GitHub account, so connector-written commits are attributed to Joe. To preserve Puck-GPT attribution, ChatGPT stages a proposed change on a temporary branch named:

- `puck-staging/direct/<name>` for direct-to-main work, or
- `puck-staging/pr/<name>` for review-first work.

A command on attribution issue #10 then triggers the repository workflow, which authenticates as the Puck-GPT GitHub App, reproduces the staged diff as a Puck-GPT-authored commit, and either pushes it to `main` or opens a Puck-GPT pull request.

The temporary staging branch is deleted after successful publication.
