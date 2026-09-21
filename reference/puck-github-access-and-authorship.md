# PUCK — GITHUB ACCESS AND AUTHORSHIP

*(Source: Puck's Library, as supplied by Joe 21 Sep 2026. Reference material — this describes Puck's mechanics, not Helen's. See the companion Helen-adapted version once drafted.)*

Inky Tech repositories covered by this protocol:

    Inky-Tech-Pty-Ltd/VillageLink
    Inky-Tech-Pty-Ltd/information-is-life
    Inky-Tech-Pty-Ltd/checklist

The Express Lane and Review Lane rules are identical in all three
repositories. Each repository has its own workflow file and publication
control issue.

## PUBLICATION CONTROLS

    VillageLink          .github/workflows/puck-publish.yml   Issue #10
    information-is-life  .github/workflows/puck-publish.yml   Issue #1
    checklist            .github/workflows/puck-publish.yml   Issue #1

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

Two GitHub Apps are installed for all three repositories:

-   ChatGPT Codex Connector: Puck can inspect repositories and prepare
    staging branches.
-   Puck-GPT: the repository workflow publishes the final commit and,
    in Review Lane, opens the PR as puck-gpt[bot].

Repository access is selected separately for each App installation.
Both installations should explicitly include all three repositories.

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

## CURRENT INFRASTRUCTURE STATUS — 20 SEPTEMBER 2026

-   VillageLink: Review and Express lanes previously demonstrated.
-   information-is-life: workflow and control Issue #1 installed;
    Review Lane verified by Puck-authored commit and PR #2.
-   checklist: workflow and control Issue #1 installed; Review Lane
    verified by Puck-authored commit and PR #2.
-   The Puck-GPT and ChatGPT Codex Connector App installations include
    all three repositories.
-   PUCK_GPT_PRIVATE_KEY is available to all three workflows.
-   All workflows reject staging branches not based on current main.
-   Smoke-test PR #2 in each newer repository preserves the verification
    trail. It may be closed without merge because its proposed file is
    only a test artefact. The staging branches were deleted automatically.

The Review Lane is operational in all three repositories. The Express
Lane is installed in all three and shares the same workflow; it has been
demonstrated in VillageLink but was not separately smoke-tested in the
two newer repositories on 20 September 2026.

## CURRENT VILLAGELINK CODE LOCATION

Repository: Inky-Tech-Pty-Ltd/VillageLink
Local working tree: C:\Users\j03ra\Documents\VillageLink\prototype
Browser source: villagelink/browser.py
Composer source: villagelink/composer.py

Before editing, locate the corresponding current GitHub branch and
files rather than inferring that prototype is a separate repository.
