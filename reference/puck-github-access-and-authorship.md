# Puck — GitHub access, authorship and publication governance

*Canonical public operating protocol. Revised 1 November 2026.*

## Current identity and authority

**Puck's GitHub machine-user account is `puck-inky`.** This identity is intended to persist independently of the intelligence supplier or model serving Puck. Its primary account email is `puck.gpt@village.link`. It is a separate GitHub user from Joe Rasmussen.

For GitHub work initiated and carried out by Puck:
- Confirm the connected GitHub principal is **`puck-inky`** using the authenticated-user endpoint **before making mutations**.
- If the principal is Joe or cannot be verified, **do not mutate** using that connection. A request from Joe is not permission to impersonate Joe.
- Use the account's delegated repository permissions; do not misrepresent the human requester, executing principal, commit author, committer, or reviewer.
- Inspect the resulting commit and PR records before claiming successful attribution. An authenticated session alone does not prove commit authorship.
- Prefer a branch and PR when review is appropriate. Direct commits are possible where repository policy permits, but should be intentional and attributable.
- GitHub's own roles, protections, approvals and audit history remain authoritative for permission decisions.

### Evidence: 1 November 2026

The GitHub connector returned authenticated login `puck-inky`, and `Inky-Tech-Pty-Ltd/VillageLink` reported Maintain permission. Puck created branch `puck-inky/issue-5-machine-user-canary`, committed a canary, and opened [draft PR #79](https://github.com/Inky-Tech-Pty-Ltd/VillageLink/pull/79). GitHub independently reported **both author and committer as `puck-inky`** on [commit `77d17f05ab9463ebfe3b3124d44fa899a4da3af2`](https://github.com/Inky-Tech-Pty-Ltd/VillageLink/commit/77d17f05ab9463ebfe3b3124d44fa899a4da3af2); PR creator was also `puck-inky`.

This is evidence of a successful *scoped* identity boundary for the connected GitHub tool. It is not a proof that every possible credential, service, dispatcher or alternate integration has been revoked. Any Joe-authenticated connection or credential capable of mutation should be separately disconnected or revoked.

## Other GitHub routes and legacy infrastructure

The **Puck-GPT GitHub App**, displayed as `puck-gpt[bot]`, and the central InkyTech Issue #1 GitHub Actions publication bus were earlier controlled publication mechanisms. They successfully produced independently attributable commits and Discussion comments, including [the reply to Cobble Discussion #8](https://github.com/Inky-Tech-Pty-Ltd/Cobble/discussions/8#discussioncomment-18915935).

These are now **legacy/alternate mechanisms, not the default publication path**. Do not dismantle the app, workflow, credentials or secrets until their users, dependencies, repository installations and decommissioning consequences have been audited. In particular, do not confuse a GitHub *App* with the human-shaped `puck-inky` machine-user account.

Historical implementation: [InkyTech Issue #1](https://github.com/Inky-Tech-Pty-Ltd/InkyTech/issues/1) and private `.github/workflows/puck-publish.yml`. Historically the bus accepted `/puck-publish` and `/puck-discussion` from authorised organisation members and published as `puck-gpt[bot]`. Check its live implementation before attempting any future use. Do not expose GitHub App private keys or secrets in chat or repositories.

## Known limitations and deferred work

- The connected GitHub connector exposes repository, issue, commit, review and PR tools but **no direct GitHub Discussions or Projects tools** as of 1 November 2026.
- Cobble MCP can read *archived* Discussion content after import. That is not a live Discussion API. The historical publication bus can publish some Discussion comments but is not the direct `puck-inky` path.
- GitHub Projects permissions may require separate grants and dedicated integrations.
- The negative identity test establishes that the tested GitHub connection acts as `puck-inky`; full assurance against impersonation requires inventory and revocation of any Joe-authenticated alternative paths.
- Decommissioning old GitHub Apps, Actions publication controls, and 1Password items is separate housekeeping, not a prerequisite for recognising successful machine-user participation.

## Governance principle

**Identity is not the intelligence provider.** Puck participates under delegated powers granted to the `puck-inky` GitHub account. A human requesting or approving work remains distinct from the identity executing the work. Keep contribution provenance inspectable, enforce boundaries with credentials and GitHub permissions rather than prompt phrasing, and preserve a safe mechanism to revoke access.

### Historical note

Older procedures involving repository-local Express/Review lanes, `puck-staging/direct/...` branches, central `/puck-publish` and `/puck-discussion` commands remain part of the historical audit trail. They are not instructions to use Joe's credentials or the default workflow for new changes.
