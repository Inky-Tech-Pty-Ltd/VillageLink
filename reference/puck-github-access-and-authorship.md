# PUCK — GITHUB ACCESS AND AUTHORSHIP

*(Operational reference — derived from Puck's Library and installed by Joe on 21 Sep 2026. This describes Puck's mechanics; the companion Helen-Claude document describes her parallel route.)*

Inky Tech project repositories covered by this local reference:

    Inky-Tech-Pty-Ltd/VillageLink
    Inky-Tech-Pty-Ltd/information-is-life

The Express Lane and Review Lane rules are identical in both repositories.
Each repository has its own workflow file and publication control issue.
The separate private checklist experiment is outside this project reference.

## PUBLICATION CONTROLS

    VillageLink          .github/workflows/puck-publish.yml   Issue #10
    information-is-life  .github/workflows/puck-publish.yml   Issue #1

## PURPOSE

This file is Puck's operational memory for accountable GitHub
authorship.

Repository changes made by Puck should appear on GitHub as:

    puck-gpt[bot]

The route by which a change enters GitHub matters. The same substantive
change can create a different authorship and history trail depending on
the publication path.

## STOP RULE — BEFORE ANY REPOSITORY WRITE

Before Puck writes repository content, decide:

    Does Joe need to review or test this change before it reaches main?

YES: Use the REVIEW LANE.

NO, and Joe has explicitly authorised the Express Lane: Use the EXPRESS
LANE.

If Joe merely says "go", treat that as approval to proceed with the
work, not as permission to choose the less-reviewed publication path.
Default ambiguous cases to the REVIEW LANE.

The ordinary GitHub connector may be used to prepare puck-staging/*.
It must not be used to publish Puck's substantive change directly to
main, to create puck/*, or to open the final review-lane PR. Those acts
belong to the Puck-GPT attribution workflow.

## GOLDEN RULE

    puck-staging/*  = where Puck puts proposed work.
    puck/*          = what the attribution workflow creates.

Puck NEVER creates puck/* itself.

Puck NEVER opens its own final Review Lane PR through the ordinary
GitHub connector. The attribution workflow creates the Puck-authored
commit and PR.

## REVIEW LANE — DEFAULT FOR SUBSTANTIVE WORK

1.  Work in the target repository and start from its current main.
2.  Stage Puck's completed change on:

        puck-staging/pr/<short-name>

3.  STOP. Tell Joe the repository and exact staging branch that are
    ready.
4.  Joe comments on that repository's publication control issue:

        /puck-publish puck-staging/pr/<short-name>

5.  .github/workflows/puck-publish.yml authenticates through the
    Puck-GPT GitHub App.
6.  The workflow verifies that the staging branch was based on current
    main.
7.  It recreates the change as a puck-gpt[bot] commit on:

        puck/<short-name>

8.  The workflow opens the PR automatically as puck-gpt[bot].
9.  The workflow deletes the staging branch.
10. Joe reviews and tests the Puck-authored PR and, if satisfied, merges
    it.

Expected trail:

    Puck stages
      -> Joe explicitly triggers publication
      -> puck-gpt[bot] authors commit
      -> puck-gpt[bot] opens PR
      -> Joe reviews/tests
      -> Joe merges

## EXPRESS LANE — ONLY WHEN EXPLICITLY AUTHORISED

1.  Work in the target repository and start from its current main.
2.  Stage Puck's completed change on:

        puck-staging/direct/<short-name>

3.  STOP. Tell Joe the repository and exact staging branch that are
    ready.
4.  Joe comments on that repository's publication control issue:

        /puck-publish puck-staging/direct/<short-name>

5.  The workflow authenticates through the Puck-GPT GitHub App.
6.  It verifies that the staging branch was based on current main.
7.  It recreates the change as a puck-gpt[bot] commit directly on main.
8.  It deletes the staging branch.

There is no PR in this lane.

## JOE'S SHORT COMMANDS

"Go — review lane" means proceed and stage the approved change on
puck-staging/pr/<short-name>. This is the default for substantive work.

"Go — express lane" means proceed and stage the approved change on
puck-staging/direct/<short-name>.

"Go" means approval to proceed with the work, but not permission to
choose the less-reviewed publication path. Default to Review Lane.

## ACCESS AND COMPONENT ROLES

Two GitHub Apps are installed for both project repositories:

-   ChatGPT Codex Connector: Puck can inspect repositories and prepare
    staging branches.
-   Puck-GPT: the repository workflow publishes the final commit and,
    in Review Lane, opens the PR as puck-gpt[bot].

Repository access is selected separately for each App installation.
Both installations should explicitly include both project repositories.

Each repository also requires the Actions secret:

    PUCK_GPT_PRIVATE_KEY

Access through the ordinary connector does not substitute for the
Puck-GPT attribution route.

## IF UNCERTAIN

STOP BEFORE PUBLISHING.

Inspect the target repository's:

-   .github/workflows/puck-publish.yml
-   publication control issue listed at the top of this file
-   recent successful Puck-GPT attribution history

Do not improvise a new publication route merely because ordinary GitHub
write tools are available.

## BOOTSTRAP OR REPAIR EXCEPTION

If a repository does not yet have working attribution plumbing, the
ordinary connector may be used to install or repair the control issue,
workflow, secret instructions, or staging test. Treat those commits as
Joe-authored infrastructure work, not as Puck-authored substantive work.
Test the repaired Review Lane before relying on it, and update this file
to record the result.

## SECURITY

Never ask Joe to paste the Puck-GPT private key into chat. Never ask Joe
to reveal PUCK_GPT_PRIVATE_KEY. Joe may copy the complete private key
directly from 1Password into the repository's GitHub Actions secret.

## CURRENT INFRASTRUCTURE STATUS — 21 SEPTEMBER 2026

-   VillageLink: Review and Express lanes demonstrated.
-   information-is-life: workflow and control Issue #1 installed; Review Lane
    verified by Puck-authored commit and PR #2. Express Lane is installed but
    has not been separately smoke-tested.
-   The Puck-GPT and ChatGPT Codex Connector App installations include both
    project repositories.
-   `PUCK_GPT_PRIVATE_KEY` is available to both workflows.
-   Both workflows reject staging branches not based on current `main`.
-   information-is-life PR #2 preserves the Review Lane verification trail and
    may remain closed because its proposed file was only a test artefact.
-   The private checklist repository is a separate experiment/catch-all and is
    not governed by these local project-reference copies.

## CURRENT VILLAGELINK CODE LOCATION

Repository: Inky-Tech-Pty-Ltd/VillageLink
Local working tree: C:\Users\j03ra\Documents\VillageLink\prototype
Browser source: villagelink/browser.py
Composer source: villagelink/composer.py

Before editing, locate the corresponding current GitHub branch and
files rather than inferring that prototype is a separate repository.


## GITHUB DISCUSSIONS — SAME PUBLICATION BUS

GitHub Discussions uses the same Puck-GPT attribution path rather than a
separate identity or control mechanism.

Control surface:

    VillageLink Issue #10

Discussion requests are staged on:

    puck-staging/discussion/<short-name>

with a request payload at:

    .puck/discussion-request.json

Joe triggers the request by commenting on Issue #10:

    /puck-discussion puck-staging/discussion/<short-name>

The Discussion workflow authenticates with the same Puck-GPT GitHub App
and publishes or reads through the GitHub Discussions GraphQL API.

Supported request operations:

-   `create` — create a Discussion as puck-gpt[bot];
-   `comment` — add a top-level comment or reply as puck-gpt[bot];
-   `edit-comment` — edit a Puck-GPT Discussion comment;
-   `read` — read a Discussion and return its thread to Issue #10.

This is an extension of the existing publication bus, not a separate
Puck identity or publication pathway. Issue #38 tracks the capability;
Issue #10 remains the control bus.

The Puck-GPT GitHub App installation must have repository Discussions
permission sufficient for these operations (write for publication).
