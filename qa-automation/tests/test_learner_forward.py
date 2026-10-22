import os
import re
import subprocess
from pathlib import Path
import pytest

PAGES = Path(__file__).resolve().parents[2] / "content/modules/ROOT/pages"

def forward_block():
    text = (PAGES / "03-prove-portability.adoc").read_text()
    return next(b for b in re.findall(r"----\n(.*?)\n----", text, re.S) if "PRAXIS_FORWARD_PID=$!" in b).replace("{project_name}", "user-synthetic-praxis")

@pytest.mark.parametrize("mode,ready", [("ready", True), ("occupied", False)])
def test_forward_readiness_and_owned_cleanup(tmp_path, mode, ready):
    binary = tmp_path / "oc"
    binary.write_text("#!/bin/bash\nif [ \"$FORWARD_MODE\" = occupied ]; then exit 1; fi\necho 'Forwarding from 127.0.0.1:8080 -> 8080'\nexec sleep 15\n".replace('\"', '"'))
    binary.chmod(0o755)
    cleanup = (PAGES / "08-conclusion.adoc").read_text()
    cleanup = next(b for b in re.findall(r"----\n(.*?)\n----", cleanup, re.S) if "kill \"$PRAXIS_FORWARD_PID\"".replace('\"', '"') in b)
    script = forward_block() + '\nif [ -n "$PRAXIS_BASE_URL" ]; then echo READY; else echo BLOCKED; fi\n' + cleanup
    result = subprocess.run(["bash", "-c", script], env=dict(os.environ, PATH=str(tmp_path) + ":" + os.environ["PATH"], FORWARD_MODE=mode), capture_output=True, text=True, timeout=40)
    assert result.returncode == 0
    assert ("READY" if ready else "BLOCKED") in result.stdout
