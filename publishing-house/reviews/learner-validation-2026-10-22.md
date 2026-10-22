# Praxis: learner validation and PH author review

Tracking: [GPTEINFRA-18273](https://issues.redhat.com/browse/GPTEINFRA-18273); [RHDPCD-2133](https://issues.redhat.com/browse/RHDPCD-2133).

## Reviewable fixes

The learner tunnel now waits for its own port-forward and stops on failure; cleanup targets the saved process instead of a broad process-name match. Both QA playbooks honor the supplied runner kubeconfig, and inference selects the configured model. Replaced the stale standalone preflight that required non-migrated catalog files with an offline PH author-package check.

## Verification boundary

10 local regression tests pass (including eight author-workspace auth checks). Antora 3.1.14 builds the current learner source. These are offline author-package results; synthetic service replies do not establish real model or catalog acceptance.

Offline readiness/occupied-port regressions and PH package preflight pass. Historical fixture startup/OAuth redirect and scoped teardown do not prove authenticated browser use or inference. No fresh real gateway-model or isolation acceptance is claimed.

## Requested reviewer actions

Assign the backend connection and generated catalog/QA identity. Validate authenticated learner UI, actual gateway inference/routing, unauthorized and second-tenant denial, negative backend/failure restoration, key revocation and timed pilot. The internal tunnel is a separate Kubernetes-authorized path, not proof of OAuth.

PH maintainers must accept the intake/design, run supported RCARS/intake ingestion and generate the AgnosticV/QA wiring. Browser PH notes are the available reconciliation channel; local API access is unavailable. Dallas and Oberon are development environments, not catalog-onboarding substitutes. Do not advance acceptance tasks or PH stages from these offline checks. Preserve the related source/reference PR history and keep every RHDP PR linked to its onboarding Jira.
