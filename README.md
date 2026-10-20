# praxis-ai-gateway

Migrate the existing Govern AI Model Access with Praxis lab into the RHDP Publishing House lifecycle. The 20–30 minute guided customer path has optional operations and governance depth up to 90 minutes. Learners use an OAuth-protected UI and a platform-managed model connection; backend credentials stay outside Showroom. Praxis is an upstream project. Preserve the existing source and AgnosticV review history while PH owns generated catalog configuration and onboarding. Tracking: GPTEINFRA-18273.

**Owner:** jkershawrh
**Migrated from:** https://github.com/jkershawrh/showroom-praxis-ai-gateway

---

## What was set up

1. Repository created (migrated from existing Showroom repo)
2. `catalog-info.yaml` added to repository
3. Registered in Developer Hub catalog
4. Orchestrator workflow started — your AI-guided content pipeline is running!

## What happens next

Claude will walk you through the entire content lifecycle — from intake and spec creation, through Jira tracking and reviews, all the way to a published lab on RHDP. Just follow the prompts!

## Getting started

### DevSpaces (recommended)

1. Open in DevSpaces: `https://devspaces.apps.ocpv-infra02.wdc07.infra.demo.redhat.com#https://github.com/rhpds/praxis-ai-gateway`
2. Use Claude via the **extension** or the **CLI**:
   - **Extension:** Click the **Claude** icon in the sidebar, click **New Session**. If the Claude icon is not visible, open **Extensions** (`Ctrl/Cmd+Shift+X`), find **Claude Code for VS Code** under the DevSpaces section, click it, then click **Enable (Workspace)**.
   - **CLI:** Open a terminal and run `claude`
3. Run `/rhdp-publishing-house` — and you're off!

### Local machine

1. Install the skills:
   ```
   git clone -b prod https://github.com/rhpds/rhdp-publishing-house-skills.git ~/.claude/skills/publishing-house
   ```
2. Clone the repo:
   ```
   git clone https://github.com/rhpds/praxis-ai-gateway
   ```
3. `cd praxis-ai-gateway`
4. Start Claude CLI: `claude`
5. Run `/rhdp-publishing-house` — and you're off!
