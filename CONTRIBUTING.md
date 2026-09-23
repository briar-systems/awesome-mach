# Contributing

Every entry is one json file in `entries/`. To add a project, add a file and open a pull request against `main`.

## Adding an entry

Name the file after the project with lowercase letters, digits, and dashes, for example `entries/mach-http.json`:

```json
{
  "name": "mach-http",
  "url": "https://github.com/briar-systems/mach-http",
  "description": "Lightweight HTTP protocol engines.",
  "category": "networking"
}
```

- `name` is the display name, usually the repository name.
- `url` is where the project lives, over https.
- `description` is one sentence ending in a period. The list is all Mach, so there is no need to say "for Mach".
- `category` is an `id` from [categories.json](categories.json). If nothing fits, add a category in the same pull request.

[schema/entry.schema.json](schema/entry.schema.json) is the full contract.

## What gets listed

Public, maintained projects written in or for Mach. Private and archived repositories are not listed, and CI rejects them.

## Checks

Pull requests run `scripts/check.py`. It validates each entry against the schema, confirms the category exists, and confirms the url is live. For GitHub repositories it also confirms they are public and not archived. To run it locally:

```sh
pip install -r requirements.txt
python scripts/check.py
```

Don't edit `README.md` or `entries.json`. A merge to `main` rebuilds both from the entries.
