# Direct GitHub write after dispatcher suspension

Date: 2026-11-01

The legacy Puck-Dispatcher GitHub App was suspended before this test. Puck verified that the connected GitHub principal was `puck-inky`, then requested this file on the existing draft PR #79 branch using the normal GitHub connector.

This canary does not assert success or attribution: those must be checked against GitHub's resulting commit metadata.
