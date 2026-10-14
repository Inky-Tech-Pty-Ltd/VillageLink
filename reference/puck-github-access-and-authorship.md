# Puck — GitHub access, authorship and publication governance

*Canonical, public operating protocol for Puck's contributions to Inky Tech GitHub repositories. Updated 14 October 2026.*

**This is the authoritative reference.** Other repositories and ChatGPT's Library should *link here*, not maintain copies. Before working on publication, inspect this document, [InkyTech Issue #1](https://github.com/Inky-Tech-Pty-Ltd/InkyTech/issues/1), and the current central workflow. Do not rely on older remembered instructions.

## Purpose and governance

Puck (an OpenAI AI collaborator) can prepare code, documents and GitHub Discussion contributions; publication is separately authorised by a human collaborator with the requisite organisational permissions.

- **Author:** substantive Puck-authored contributions are attributed to the **Puck-GPT GitHub App**, displayed as `puck-gpt[bot]`.
- **Authoriser:** an **Inky Tech organisation member** holding **Write, Maintain or Admin** effective permission on the **InkyTech** repository may invoke the central publication workflow.
- **Source of authority:** the organisation's current GitHub membership and repository permissions—not a hard-coded list of names, and not personal approval by Joe Rasmussen.
- **Audit trail:** the issue command identifies the human requesting publication; GitHub records the resulting bot-attributed action and the workflow's reported outcome.
- **Revocation:** removing the member's qualifying access is intended to remove the ability to authorise a future publication. Permission changes do not undo publications already made.

These are *delegated publication powers*, not a claim that Puck has independent governance authority. A person authorised to publish must still exercise judgement about the proposed content and its consequences.

The workflow checks both the commenter's GitHub author association (`MEMBER` or `OWNER`) and their effective InkyTech permission via GitHub's API. For `/puck-publish` and `/puck-discussion`, permitted effective permissions are `write`, `maintain`, or `admin`. **The expanded membership-based gate has been published but needs an end-to-end test by a second authorised member**, such as Sankarshan.

## The central publication bus

- **Control surface:** [InkyTech Issue #1](https://github.com/Inky-Tech-Pty-Ltd/InkyTech/issues/1).
- **Implementation:** InkyTech's private `.github/workflows/puck-publish.yml`.
- **Bot identity:** the **Puck-GPT** GitHub App, authenticated inside GitHub Actions with a secret. Its private key must **never** be provided in chat or committed to a repository.
- **Current allowlist:** `VillageLink`, `Cobble`, `information-is-life`, `InkyTech`. `InkyBooks` is **not** currently allowlisted.
- **Scope:** authorisation on *InkyTech* confers the ability to trigger the bus for **any allowlisted destination repository**. It does not depend on Write access to the target repository itself; the Puck-GPT App must have the necessary target-repository permissions.

The implementation is private, but the **governance and protocol are deliberately documented publicly** here. The allowlist, permissions, workflow logic and security posture must be checked against current configuration if changed.

## Publish a Puck-authored repository change

1. Puck prepares changes in the destination repository on a branch named `puck-staging/direct/<short-name>`, based on current `main`.
2. Puck reports the repository, branch and intended change. A human with publication authority reviews as appropriate.
3. That human comments on [InkyTech Issue #1](https://github.com/Inky-Tech-Pty-Ltd/InkyTech/issues/1):

   ```text
   /puck-publish <repo> puck-staging/direct/<short-name>
   ```

   For the InkyTech repository itself, `/puck-publish puck-staging/direct/<short-name>` is also supported.
4. The workflow checks authority and an allowlisted destination, confirms the staging branch shares current `main` as its base, reproduces the staged change in a Puck-GPT-attributed commit directly on `main`, deletes the source branch, and comments on Issue #1.

**Express publication is the established route.** Use an ordinary branch/PR when human review or testing warrants one; the former custom *Review Lane* is not the current publication protocol. Puck must not bypass the attribution workflow by publishing substantive contributions directly using the ordinary GitHub connector.

## Publish a Puck-authored GitHub Discussion comment

1. Puck creates a target-repository branch `puck-staging/discussion/<short-name>` based on current `main`.
2. On that branch Puck writes `.puck/discussion-request.json`:

   ```json
   {
     "operation": "comment",
     "discussion_number": 8,
     "body": "The full Markdown reply, including Puck's attribution."
   }
   ```

3. An authorised InkyTech member comments on [InkyTech Issue #1](https://github.com/Inky-Tech-Pty-Ltd/InkyTech/issues/1):

   ```text
   /puck-discussion <repo> puck-staging/discussion/<short-name>
   ```

4. The central workflow validates the request, resolves the destination Discussion via GitHub GraphQL, publishes as `puck-gpt[bot]`, posts the URL on Issue #1, and removes the staging branch on success.

**Current central Discussion capability: top-level `comment` only.** Older, repository-local VillageLink Discussion plumbing supported additional operations (`create`, `edit-comment`, `read`), but **those are not presently supported by the central InkyTech command**. Do not assume they work centrally.

### First Cobble Discussion publication

On 14 October 2026, Puck retrieved [Sankarshan's Cobble Discussion #8](https://github.com/Inky-Tech-Pty-Ltd/Cobble/discussions/8) through Cobble's `read_github_discussion` MCP tool using an archived copy on McKay, not a live GitHub read. Puck then prepared a response for the central publishing bus. Joe triggered publication, which produced [this `puck-gpt[bot]` comment](https://github.com/Inky-Tech-Pty-Ltd/Cobble/discussions/8#discussioncomment-18915935).

That demonstrates independently stored content being retrieved through Cobble and a separately authorised, attributed publication. It does **not** establish successful graph-assisted retrieval, AI identity continuity or autonomous governance.

## Controls, limitations and operational hygiene

- **Consult before acting:** inspect the canonical document, actual workflow and control issue. Earlier copies in other repositories or Library may be stale.
- **Never assert publication before confirmation:** check the control-issue result and resulting GitHub artifact.
- **Validate permissions:** the new org-member authorisation should be smoke-tested with a second member and with a non-authorised user; failure is a reason to repair the gate, not bypass it.
- **Handle stale staging branches:** if the target `main` has advanced, restage on current `main` before triggering again.
- **Protect the bus:** access to InkyTech with Write or higher conveys cross-repository Puck publication authority. This is a meaningful organisational delegation, not merely ordinary contribution rights.
- **Don't confuse facts and assertions:** Village Links encode published equivalence claims, not guaranteed truth. Puck must preserve the distinction when citing evidence or publishing claims.

### Historical note

Before October 2026, repository-local publication workflows, VillageLink Issue #10 and dedicated Express/Review Lanes were used. Those instructions are historical; **the current route is InkyTech Issue #1**. The separate Helen-Claude authorship arrangement is outside this protocol.
