"""Offline PH author-package preflight, not generated-catalog acceptance."""
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "content/modules/ROOT/pages"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


for name in ("default-site.yml", "ui-config.yml", "content/antora.yml",
             "publishing-house/spec.yaml", "automation/ansible/galaxy.yml",
             "automation/ansible/roles/configure_praxis/tasks/main.yml",
             "automation/gitops/praxis/Chart.yaml", "automation/gitops/bootstrap-infra/Chart.yaml",
             "qa-automation/healthcheck.yml", "qa-automation/e2e.yml"):
    require((ROOT / name).is_file(), f"Author package is missing {name}")
nav = (ROOT / "content/modules/ROOT/nav.adoc").read_text()
for target in re.findall(r"xref:([^\[]+)", nav):
    require((PAGES / target).is_file(), f"Missing navigation target: {target}")
for page in sorted(PAGES.glob("0[2-7]-*.adoc")):
    text = page.read_text()
    for heading in ("== Customer outcome", "== Know:", "== Show:", "== Customer discussion", "== Evidence", "== Key takeaway"):
        require(heading in text, f"{page.name} lacks {heading}")
ui = yaml.safe_load((ROOT / "ui-config.yml").read_text())
require({tab["name"] for tab in ui["tabs"]} == {"Terminal", "App UI", "OCP Console"}, "Incomplete UI tabs")
spec = yaml.safe_load((ROOT / "publishing-house/spec.yaml").read_text())
require(spec["project"]["deployment_mode"] == "rhdp_published", "Incorrect PH deployment mode")
for name in ("healthcheck.yml", "e2e.yml"):
    plays = yaml.safe_load((ROOT / "qa-automation" / name).read_text())
    for play in plays:
        require(play["module_defaults"]["group/kubernetes.core.k8s"]["kubeconfig"] == "{{ k8s_kubeconfig | default(omit) }}", "QA must use the supplied runner kubeconfig")
print("PASS: PH author package preflight; live learner and generated catalog acceptance remain pending")
