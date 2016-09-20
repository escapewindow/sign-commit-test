#!/usr/bin/env python
"""Check the signatures on git commits.

As currently written, the latest non-merge-commit must be signed.  If you sign
a commit, you're signing off on all changes since the last signed commit.
"""
import subprocess
import sys

VALID_KEY_IDS = {
    "FC829B7FFAA9AC38": "asasaki@mozilla.com",
}

def main(name=None):
    if name not in (None, "__main__"):
        return
    output = subprocess.check_output(
        ["git", "log", "--no-merges", "--format='%H:%GK'"]
    ).decode('utf-8')
    message = "Unknown exception"
    for line in output.splitlines():
        sha, keyid = line.replace("'", "").split(':')
        if not keyid:
            message = "Latest commit {} is not signed!\nCommits must be gpg signed: `git commit -S[<keyid>]`".format(sha)
            break
        if keyid not in VALID_KEY_IDS.keys():
            message = "Latest commit {} is signed by an invalid key {}!".format(sha, keyid)
            break
        print("{} is signed by {} ({})".format(sha, keyid, VALID_KEY_IDS[keyid]))
        sys.exit(0)
    raise Exception(message)


main(name=__name__)
