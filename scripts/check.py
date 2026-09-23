"""checks every entry against the schema and categories, then that each url is
live. github repos must also be public and not archived. exits 1 on any problem.

usage: check.py [--offline]
"""
import json
import os
import sys
import urllib.error
import urllib.request

import listing

UA = "awesome-mach-check"


def request(url, method="GET", headers=None):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, **(headers or {})})
    return urllib.request.urlopen(req, timeout=20)


def github_problem(owner, repo, token):
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        with request(f"https://api.github.com/repos/{owner}/{repo}", headers=headers) as res:
            meta = json.load(res)
    except urllib.error.HTTPError as e:
        return "repository not found or not public" if e.code == 404 else f"github api returned {e.code}"
    if meta.get("private"):
        return "repository is private"
    if meta.get("archived"):
        return "repository is archived"
    return None


def web_problem(url):
    # some hosts refuse HEAD, so fall back to GET before calling a link dead
    for method in ("HEAD", "GET"):
        try:
            with request(url, method=method):
                return None
        except urllib.error.HTTPError as e:
            last = f"returned {e.code}"
        except (urllib.error.URLError, TimeoutError) as e:
            last = f"unreachable: {getattr(e, 'reason', e)}"
    return last


def url_problem(url, token):
    m = listing.GITHUB_REPO.match(url)
    return github_problem(m.group(1), m.group(2), token) if m else web_problem(url)


def main(argv):
    categories, entries, problems = listing.load()
    if "--offline" not in argv:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        for e in entries:
            p = url_problem(e["url"], token)
            if p:
                problems.append(f"entries/{e['id']}.json: {e['url']}: {p}")
    for p in problems:
        print(f"error: {p}", file=sys.stderr)
    print(f"checked {len(entries)} entries in {len(categories)} categories, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
