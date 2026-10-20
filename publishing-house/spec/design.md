# Govern AI Model Access with Praxis

## Delivery ownership

Migrate the existing Govern AI Model Access with Praxis lab into the RHDP Publishing House lifecycle. The 20–30 minute guided customer path has optional operations and governance depth up to 90 minutes. Learners use an OAuth-protected UI and a platform-managed model connection; backend credentials stay outside Showroom. Praxis is an upstream project. Preserve the existing source and AgnosticV review history while PH owns generated catalog configuration and onboarding. Tracking: GPTEINFRA-18273.

PH owns intake, reviews, Env Setup, generated AgnosticV and onboarding. Existing catalog PRs are historical proposals for reference; they are not a parallel onboarding route. Dallas OCP 4.18.16 is a development test environment. The proposed published target is OCP 4.22, subject to PH infrastructure acceptance.

## Learner path

1. Orient to the customer experience (5 min).
2. Show governed model access (10 min).
3. Prove the application boundary (15 min).
4. Correlate evidence for one request (15 min).
5. Discuss failure and recovery (15 min).
6. Assess isolation and data controls (15 min).
7. Map the customer architecture (15 min).

## Infrastructure and credential boundary

One assigned tenant namespace and tenant-scoped model access. No learner GPU or local model server is provisioned in the guided profile. Max 25 concurrent learners is a capacity proposal requiring validation, not a tested result. Preserve namespace isolation, short-lived key creation/revocation and workload-owned cleanup.

## Acceptance and evidence

Validate deployed images and terminal dependencies, then real model access and the full learner workflow. Record source/image revisions, failure behavior, tenant isolation and cleanup. CPU placement requires serving-team evidence. Remaining RCARS overlap review, model allocation, capacity and author acceptance are explicit intake gates.

Tracking: RHDPCD-2133; GPTEINFRA-18273.
