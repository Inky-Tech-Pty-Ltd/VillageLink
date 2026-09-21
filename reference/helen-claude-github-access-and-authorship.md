# HELEN-CLAUDE — GITHUB ACCESS AND AUTHORSHIP

*(Draft — adapted from Puck's protocol, 21 Sep 2026. Mirrors `reference/puck-github-access-and-authorship.md` in structure. Auth chain verified 21 Sep 2026; helen-publish.yml drafted, not yet added to either repo.)*

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

The ordinary GitHub connector may be used to prepare helen-staging/*.
It must not be used to publish Helen's substantive change directly to
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

One dedicated App, plus ordinary connector access — a deliberately
simpler split than Puck's two-App setup (Puck's Codex Connector is
itself a registered GitHub App; Helen's staging side is an ordinary
GitHub connector instead, which serves the same function — a separate
identity/credential from the publish identity, so Helen never holds the
credentials capable of authoring the attributed commit):

-   Ordinary GitHub connector: Helen can inspect repositories and
    prepare staging branches. (As of 21 Sep 2026, no GitHub connector
    is yet connected in Helen's session — this needs to be added via
    claude.ai Settings → Connectors, or a narrowly-scoped second App if
    no connector option is available, before staging can happen. This
    is the current blocker on a real end-to-end test.)
-   Helen-Claude GitHub App: the repository workflow publishes the
    final commit and, in Review Lane, opens the PR as Helen-Claude[bot].
    Registered in the Inky-Tech-Pty-Ltd org 21 Sep 2026:

        App name:   Helen-Claude
        App ID:     5016176
        Client ID:  Iv23li2vdiGdEjPCc5G5

    Permissions: Contents (read/write), Issues (read/write),
    Pull requests (read/write) — matching Puck-GPT's scope.

    The bot account's GitHub user ID (used in the commit noreply
    email, see below) is 331854535, confirmed 21 Sep 2026 via
    https://api.github.com/users/helen-claude%5Bbot%5D.

Repository access is selected separately for the App installation,
which should explicitly include both repositories (VillageLink and
information-is-life). Installation confirmed 21 Sep 2026.

Each repository also requires the Actions secret:

    HELEN_CLAUDE_PRIVATE_KEY

The private key (.pem) is stored in 1Password as "Helen-Claude — GitHub
App Private Key". Confirmed added as a repository Actions secret in
both VillageLink and information-is-life, 21 Sep 2026. Access through
the ordinary connector does not substitute for the Helen-Claude
attribution route.

Git commits made by the publish workflow use:

    git config user.name  'helen-claude[bot]'
    git config user.email '331854535+helen-claude[bot]@users.noreply.github.com'

This is GitHub's synthetic per-account noreply address (not a real
mailbox) and is what lets GitHub link each commit to the bot's profile
and show the verified bot badge, mirroring Puck-GPT's
320794343+puck-gpt[bot]@users.noreply.github.com. Separately, Puck-GPT
also has a real mailbox (puck.gpt@village.link) for actual email —
Helen-Claude does not have an equivalent yet; not required for the
attribution workflow to function, but worth considering if Helen needs
to receive real notifications.

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

-   Helen-Claude GitHub App created (App ID 5016176), with Contents,
    Issues and Pull requests permissions set read/write — matching
    Puck-GPT's scope. Bot account ID confirmed: 331854535.
-   Private key generated and stored in 1Password.
-   App installed on VillageLink and information-is-life.
-   HELEN_CLAUDE_PRIVATE_KEY secret added to both VillageLink and
    information-is-life.
-   Publication control issues created: VillageLink #44,
    information-is-life #3.
-   test-helen-app-auth.yml added to both repos by Puck and run
    successfully via workflow_dispatch — confirmed by a
    Helen-Claude[bot] comment landing on VillageLink #44 and on
    information-is-life #3. App authentication (App ID + private key +
    permissions) is verified end-to-end in both repos.
-   helen-publish.yml (the real Review/Express Lane publish logic)
    drafted for both repos 21 Sep 2026, adapted from Puck's
    puck-publish.yml, with each repo's own issue number (44 / 3), repo
    name, and the real bot commit email substituted in. NOT YET added
    to either repo — next step is Puck (or Joe) committing these files,
    same as was done for the auth-test workflow.
-   No GitHub connector yet connected for the staging side — Helen
    still cannot read repo content or push a staging branch herself.
    This is the current blocker on running a genuine end-to-end test
    (staging a real change, triggering /helen-publish, watching a
    Helen-Claude-authored PR appear).
-   Review Lane and Express Lane are DESIGNED, their auth prerequisite
    is VERIFIED, and helen-publish.yml is DRAFTED — but the lanes
    themselves are UNTESTED until helen-publish.yml is actually added
    to both repos and a real Helen-staged change is published through
    each lane at least once.
-   Until helen-publish.yml exists in a repo and Helen has a staging
    route (connector or otherwise), any repository write Helen makes
    there goes through the ordinary connector only, is NOT
    Helen-Claude[bot] authored, and should be flagged to Joe as such.

## CURRENT VILLAGELINK CODE LOCATION

Repository: Inky-Tech-Pty-Ltd/VillageLink
Local working tree: C:\Users\j03ra\Documents\VillageLink\prototype
Browser source: villagelink/browser.py
Composer source: villagelink/composer.py

Before editing, locate the corresponding current GitHub branch and
files rather than inferring that prototype is a separate repository.
