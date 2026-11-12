# HELEN-CLAUDE — GITHUB ACCESS AND AUTHORSHIP

*(Operational reference — adapted from Puck's protocol, 21 Sep 2026. Mirrors `reference/puck-github-access-and-authorship.md` in structure. Authentication and publication workflows are installed in both repositories; the first end-to-end Helen-authored Review Lane changes were successfully published as PRs on 21 Sep 2026.)*

Inky Tech repositories covered by this protocol:

    Inky-Tech-Pty-Ltd/VillageLink
    Inky-Tech-Pty-Ltd/information-is-life

(The "checklist" repo was an experiment that hasn't worked out and is
out of scope for this protocol. Puck's doc still covers three repos;
Helen's covers these two.)

The Express Lane and Review Lane rules are identical in both
repositories. Each repository has its own workflow file and publication
control issue, separate from Puck's.

## PUBLICATION CONTROLS

    VillageLink          .github/workflows/helen-publish.yml   Issue #44
    information-is-life  .github/workflows/helen-publish.yml   Issue #3

(Separate from Puck's control issues so `/helen-publish` and
`/puck-publish` never collide on the same thread.)

## PURPOSE

This file is Helen-Claude's operational memory for accountable GitHub
authorship, run in parallel with — but independent of — Puck's.

Repository changes made by Helen should appear on GitHub as:

    Helen-Claude[bot]

The route by which a change enters GitHub matters. The same substantive
change can create a different authorship and history trail depending on
the publication path.

## STOP RULE — BEFORE ANY REPOSITORY WRITE

Before Helen writes repository content, decide:

    Does Joe need to review or test this change before it reaches main?

YES: Use the REVIEW LANE.

NO, and Joe has explicitly authorised the Express Lane: Use the EXPRESS
LANE.

If Joe merely says "go", treat that as approval to proceed with the
work, not as permission to choose the less-reviewed publication path.
Default ambiguous cases to the REVIEW LANE.

Claude Code may be used to prepare helen-staging/*. It must not be
used to publish Helen's substantive change directly to
main, to create helen/*, or to open the final review-lane PR. Those acts
belong to the Helen-Claude attribution workflow.

## GOLDEN RULE

    helen-staging/*  = where Helen puts proposed work.
    helen/*          = what the attribution workflow creates.

Helen NEVER creates helen/* itself.

Helen NEVER opens its own final Review Lane PR through the ordinary
GitHub connector. The attribution workflow creates the Helen-Claude
commit and PR.

## REVIEW LANE — DEFAULT FOR SUBSTANTIVE WORK

1.  Work in the target repository and start from its current main.
2.  Stage Helen's completed change on:

        helen-staging/pr/<short-name>

3.  STOP. Tell Joe the repository and exact staging branch that are
    ready.
4.  Joe comments on that repository's publication control issue:

        /helen-publish helen-staging/pr/<short-name>

5.  .github/workflows/helen-publish.yml authenticates through the
    Helen-Claude GitHub App.
6.  The workflow verifies that the staging branch was based on current
    main.
7.  It recreates the change as a Helen-Claude[bot] commit on:

        helen/<short-name>

8.  The workflow opens the PR automatically as Helen-Claude[bot].
9.  The workflow deletes the staging branch.
10. Joe reviews and tests the Helen-Claude-authored PR and, if
    satisfied, merges it.

Expected trail:

    Helen stages
      -> Joe explicitly triggers publication
      -> Helen-Claude[bot] authors commit
      -> Helen-Claude[bot] opens PR
      -> Joe reviews/tests
      -> Joe merges

## EXPRESS LANE — ONLY WHEN EXPLICITLY AUTHORISED

1.  Work in the target repository and start from its current main.
2.  Stage Helen's completed change on:

        helen-staging/direct/<short-name>

3.  STOP. Tell Joe the repository and exact staging branch that are
    ready.
4.  Joe comments on that repository's publication control issue:

        /helen-publish helen-staging/direct/<short-name>

5.  The workflow authenticates through the Helen-Claude GitHub App.
6.  It verifies that the staging branch was based on current main.
7.  It recreates the change as a Helen-Claude[bot] commit directly on
    main.
8.  It deletes the staging branch.

There is no PR in this lane.

## JOE'S SHORT COMMANDS

"Go — review lane" means proceed and stage the approved change on
helen-staging/pr/<short-name>. This is the default for substantive work.

"Go — express lane" means proceed and stage the approved change on
helen-staging/direct/<short-name>.

"Go" means approval to proceed with the work, but not permission to
choose the less-reviewed publication path. Default to Review Lane.

## ACCESS AND COMPONENT ROLES

Two deliberately separate execution paths are used:

-   Claude Code provides the staging workspace. It may inspect the
    repository, prepare changes, and push `helen-staging/*` branches. Its
    staging identity is not treated as the final authorship record.
-   The Helen-Claude GitHub App provides publication identity. The
    repository workflow recreates the staged diff as a
    `Helen-Claude[bot]` commit and, in Review Lane, opens the PR.

This separation means Helen's working environment never needs the private key
that authors the attributed commit.

The Helen-Claude GitHub App is registered in the Inky-Tech-Pty-Ltd
organization:

    App name:   Helen-Claude
    App ID:     5016176
    Client ID:  Iv23li2vdiGdEjPCc5G5

Permissions: Contents (read/write), Issues (read/write), and Pull requests
(read/write). The App installation explicitly includes `VillageLink` and
`information-is-life`.

Each repository requires the Actions secret:

    HELEN_CLAUDE_PRIVATE_KEY

The private key is stored in 1Password as "Helen-Claude — GitHub App Private
Key" and was added as a repository Actions secret in both repositories on
21 Sep 2026.

Git commits made by the publish workflow use:

    git config user.name  'helen-claude[bot]'
    git config user.email '331854535+helen-claude[bot]@users.noreply.github.com'

The bot account ID and noreply address were confirmed on 21 Sep 2026. The
address exists for GitHub attribution; it is not a mailbox.

## IF UNCERTAIN

STOP BEFORE PUBLISHING.

Inspect the target repository's:

-   .github/workflows/helen-publish.yml
-   publication control issue listed at the top of this file
-   recent successful Helen-Claude attribution history

Do not improvise a new publication route merely because ordinary GitHub
write tools are available.

## BOOTSTRAP OR REPAIR EXCEPTION

If a repository does not yet have working attribution plumbing, the
ordinary connector may be used to install or repair the control issue,
workflow, secret instructions, or staging test. Treat those commits as
Joe-authored infrastructure work, not as Helen-authored substantive
work. Test the repaired Review Lane before relying on it, and update
this file to record the result.

## SECURITY

Never ask Joe to paste the Helen-Claude private key into chat. Never
ask Joe to reveal HELEN_CLAUDE_PRIVATE_KEY. Joe may copy the complete
private key directly from 1Password into the repository's GitHub
Actions secret.

## VISUAL IDENTITY

A signature-style monogram mark (italic "H" with a gold quill-flourish
tail into a small cursive "c") was designed 21 Sep 2026 for use as the
Helen-Claude App's avatar — distinct from Inky Tech's default "Inky
Skink" mascot and from Puck-GPT's identity. Not yet uploaded as the
App's profile photo in GitHub App settings (Settings → Developer
settings → GitHub Apps → Helen-Claude → upload under "Display
information").

## CURRENT INFRASTRUCTURE STATUS — 21 SEPTEMBER 2026

-   Helen-Claude GitHub App created, installed on `VillageLink` and
    `information-is-life`, and granted Contents, Issues, and Pull requests
    read/write permissions.
-   Private key stored in 1Password; `HELEN_CLAUDE_PRIVATE_KEY` added to both
    repositories.
-   Publication controls created: VillageLink Issue #44 and
    information-is-life Issue #3.
-   `test-helen-app-auth.yml` installed and successfully run in both
    repositories. Helen-Claude[bot] comments on the control issues verify the
    App ID, private key, and permissions chain end to end.
-   `helen-publish.yml` installed in both repositories by Puck on
    21 Sep 2026.
-   Root `CLAUDE.md` staging instructions and the local `reference/`
    protocol copies are installed in both repositories.
-   Claude Code staging access is available. The bootstrap documentation was
    committed as Joe-authored infrastructure, consistent with the bootstrap
    exception above.
-   Review Lane was successfully exercised in both repositories with genuine
    Helen-staged access-test changes. The workflows recreated the staged diffs
    as `Helen-Claude[bot]` commits and automatically opened VillageLink PR #46
    and information-is-life PR #4.
-   The two access-test PRs remain open for Joe's review and merge.
-   Express Lane remains untested and can be smoke-tested separately if useful.

## CURRENT VILLAGELINK CODE LOCATION

Repository: Inky-Tech-Pty-Ltd/VillageLink
Local working tree: C:\Users\j03ra\Documents\VillageLink\prototype
Browser source: villagelink/browser.py
Composer source: villagelink/composer.py

Before editing, locate the corresponding current GitHub branch and
files rather than inferring that prototype is a separate repository.
