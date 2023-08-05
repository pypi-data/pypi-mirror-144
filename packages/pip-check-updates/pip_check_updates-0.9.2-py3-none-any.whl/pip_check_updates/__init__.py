import itertools
import re
from pathlib import Path

import requests


def get_latest_version(name, no_ssl_verify):
    r = requests.get(f"https://pypi.org/pypi/{name}/json", verify=not no_ssl_verify)
    if r.status_code == 200:
        version = r.json()["info"]["version"]
        return version
    return None


def get_current_version(dep):
    name, current_version = [token for token in re.split(r"[><=~!]", dep) if token]
    op = dep[len(name) : -len(current_version)]
    return name, current_version, op


def compare_versions(current_version, latest_version):
    current_versioning = current_version.split(".")
    latest_versioning = latest_version.split(".")

    max_size = max(len(current_versioning), len(latest_versioning))
    if max_size < 3:
        max_size = 3

    current_versioning = current_versioning + ["0"] * (
        max_size - len(current_versioning)
    )
    latest_versioning = latest_versioning + ["0"] * (max_size - len(latest_versioning))

    if latest_versioning == current_versioning:
        return None

    if latest_versioning[0] != current_versioning[0]:
        return "major"

    if latest_versioning[1] != current_versioning[1]:
        return "minor"

    if latest_versioning[2] != current_versioning[2]:
        return "patch"

    return "other"


def load_dependencies(path="requirements.txt", recursive=True):
    p = Path(path).resolve()
    deps = []
    with open(p) as f:
        for dep in f.read().splitlines():
            dep = re.sub(r"#.*", "", dep).strip()
            dep = re.sub(r"{%.*?%}", "", dep).strip()
            dep = re.sub(r"{{.*?}}", "", dep).strip()
            if not dep:
                continue
            if dep.startswith("-r") and recursive:
                deps.extend(
                    load_dependencies(
                        p.parent / dep.partition("-r")[-1].strip(),
                        recursive,
                    )
                )
                continue
            if dep.startswith("-f"):
                continue
            try:
                name, current_version, op = get_current_version(dep)
                deps.append([p, name, current_version, op])
            except:
                pass

    deps = list(dep for dep, _ in itertools.groupby(deps))

    return deps
