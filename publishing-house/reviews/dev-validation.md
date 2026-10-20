# Dev validation evidence

## Development validation — 2026-10-20

Dallas OCP 4.18.16 is a dev environment, separate from the proposed published target. Tests did not order a catalog item or establish published-lab acceptance. Existing dev model credentials were used only in memory for short synthetic requests; they were not copied into fixture workloads.

- Ansible fixture provisioning PASS; no real model credential was injected.
- Gateway and OAuth/UI deployments ready after correcting probes and required OAuth/API egress.
- `/oauth/start` returns an OAuth authorization redirect (302). Root 403 is not a failed redirect assertion.
- Namespace-scoped OAuth authorization is rendered; authenticated learner and cross-tenant denial tests remain pending.
- Gateway inference remains pending. Proposed model `granite-3-2-8b-instruct` is absent from the existing dev allocation; the `-cpu` alias is a separate allocation, not proof of published compatibility.

Source fixes and this migration draft need author/reviewer acceptance. No workstream is marked complete.

Scoped teardown PASS: only the role-owned two Secrets and ConfigMap were removed; the tenant namespace and unrelated sentinel were preserved. The task then removed its three disposable dev namespaces. This is not proof of real virtual-key revocation.

Scoped teardown PASS: the role removed only its two Secrets and ConfigMap, preserving the namespace and unrelated sentinel. All three task-created dev namespaces were then removed. This does not establish real virtual-key revocation.
