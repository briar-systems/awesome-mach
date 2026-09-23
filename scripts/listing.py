"""loads and checks the list data. shared by check.py and build.py."""
import json
import re
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parent.parent
ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")
GITHUB_REPO = re.compile(r"^https://github\.com/([^/\s]+)/([^/\s]+?)/?$")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validator(name, root=ROOT):
    schema = load_json(root / "schema" / name)
    return jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())


def load(root=ROOT):
    """returns (categories, entries, problems). entries carry their id."""
    problems = []

    cats_path = root / "categories.json"
    cats_doc = load_json(cats_path)
    for err in validator("categories.schema.json", root).iter_errors(cats_doc):
        problems.append(f"categories.json: {err.json_path}: {err.message}")
    categories = cats_doc.get("categories", []) if isinstance(cats_doc, dict) else []
    known = {c.get("id") for c in categories if isinstance(c, dict)}

    entry_schema = validator("entry.schema.json", root)
    entries = []
    for path in sorted((root / "entries").iterdir()):
        rel = f"entries/{path.name}"
        if path.suffix != ".json" or not ID.match(path.stem):
            problems.append(f"{rel}: file name must be <id>.json with a lowercase id of letters, digits, and dashes")
            continue
        try:
            doc = load_json(path)
        except json.JSONDecodeError as e:
            problems.append(f"{rel}: invalid json: {e}")
            continue
        errors = list(entry_schema.iter_errors(doc))
        for err in errors:
            problems.append(f"{rel}: {err.json_path}: {err.message}")
        if errors:
            continue
        if doc["category"] not in known:
            problems.append(f"{rel}: unknown category '{doc['category']}', see categories.json")
            continue
        entries.append({"id": path.stem, **doc})

    return categories, entries, problems


def ordered(categories, entries):
    """entries grouped by category order, then by name."""
    rank = {c["id"]: i for i, c in enumerate(categories)}
    return sorted(entries, key=lambda e: (rank[e["category"]], e["name"].lower(), e["id"]))
