"""Resolve packaged code and native runtimes without relocating user data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATHS = json.loads((ROOT / 'bin/btools-paths.json').read_text())

def path(original):
    if original == '/usr/bin':
        return str(ROOT / 'bin')
    return str(ROOT / PATHS[original]) if original in PATHS else original

def manifest(filename):
    def expand(value):
        if isinstance(value, dict):
            return {path(key): expand(item) for key, item in value.items()}
        if isinstance(value, list):
            return [expand(item) for item in value]
        return path(value) if isinstance(value, str) else value
    return expand(json.loads(Path(filename).read_text()))
