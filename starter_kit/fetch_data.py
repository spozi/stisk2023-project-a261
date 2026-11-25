"""Download your project's raw data. Edit only the SOURCES dictionary.

Run it from your project folder:

    python fetch_data.py

Every file listed in SOURCES is saved in data/raw/ exactly as the publisher serves it.
data/raw/MANIFEST.json records where each file came from, when it was downloaded, its
size and its SHA-256 hash (a fingerprint of the file's bytes).

Running the script again downloads only missing files. Files already saved are checked
against the manifest, so you will know if one was changed by mistake. Never edit a raw
file: all cleaning happens in code (src/clean.py).

The starter kit comes with the EXAMPLE file (weekly fuel prices) already downloaded.
To switch to your own data: replace SOURCES, delete everything in data/raw/ (including
MANIFEST.json), and run this script again.
"""

import hashlib
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# One entry per raw file: the name to save it under in data/raw/, and where it comes from.
# "url" must be a direct link to the file (CSV, JSON, Excel or parquet), with no login.
# A source that needs a login (for example Kaggle) needs approval at Checkpoint 1. Save it
# in data/raw/ by hand and add "manual": True; the script then records it without downloading.
SOURCES = {
    "fuelprice.csv": {  # EXAMPLE: replace with your own source(s)
        "url": "https://storage.data.gov.my/commodities/fuelprice.csv",
        "page": "https://data.gov.my/data-catalogue/fuelprice",
        "publisher": "Ministry of Finance (MOF), published on data.gov.my",
        "licence": "CC BY 4.0",
    },
}

DATA_DIR = Path(__file__).resolve().parent / "data" / "raw"
MANIFEST_NAME = "MANIFEST.json"


def sha256_of(path: Path) -> str:
    """Return the SHA-256 hex digest of a file."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, destination: Path) -> None:
    """Save the bytes served at url to destination, replacing it only when the download is complete."""
    request = urllib.request.Request(url, headers={"User-Agent": "STISK2023-student-project"})
    partial = destination.with_name(destination.name + ".part")
    try:
        with urllib.request.urlopen(request, timeout=120) as response, open(partial, "wb") as handle:
            for block in iter(lambda: response.read(1 << 20), b""):
                handle.write(block)
    except (urllib.error.URLError, TimeoutError) as error:
        partial.unlink(missing_ok=True)
        raise RuntimeError(
            f"Could not download {url}. Check the link in a browser and your connection, then try again."
        ) from error
    partial.replace(destination)


def fetch_all(data_dir: Path = DATA_DIR) -> dict:
    """Download any missing file, check saved files against the manifest, and return the manifest."""
    data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = data_dir / MANIFEST_NAME
    old = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    old_files = old.get("files", {})
    files = {}

    for name, source in SOURCES.items():
        path = data_dir / name
        entry = old_files.get(name)
        if path.exists() and entry is not None:
            if sha256_of(path) != entry["sha256"]:
                raise RuntimeError(
                    f"data/raw/{name} no longer matches MANIFEST.json. Raw files must never be edited. "
                    "Restore the file from your team's copy, or delete it and run fetch_data.py again."
                )
            files[name] = entry
            continue
        if source.get("manual"):
            if not path.exists():
                raise FileNotFoundError(f"{name} is marked manual: save it in data/raw/ by hand first.")
            print(f"Recording {name} (added by hand) ...", flush=True)
            retrieved = "added by hand; see the data card for the date"
        else:
            print(f"Downloading {name} ...", flush=True)
            download(source["url"], path)
            retrieved = datetime.now(timezone.utc).isoformat(timespec="seconds")
        files[name] = {
            **{key: value for key, value in source.items() if key != "manual"},
            "retrieved_at_utc": retrieved,
            "bytes": path.stat().st_size,
            "sha256": sha256_of(path),
        }

    dropped = sorted(set(old_files) - set(SOURCES))
    if dropped:
        print("No longer in SOURCES, removed from the manifest:", ", ".join(dropped))
    manifest = {"files": files}
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DATA_DIR
    result = fetch_all(target)
    for name, entry in result["files"].items():
        print(f"{name:30} {entry['bytes']:>12,} bytes  retrieved {entry['retrieved_at_utc']}")
