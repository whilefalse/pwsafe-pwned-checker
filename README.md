# pwsafe2lastpass

A simple tool to export passwords from a pwSafe3 database into a CSV format compatible with LastPass import.

## Usage

    pip install -t requirements.txt
    python dump.py <path-to-db.pwsafe3> | pbcopy

Then go to LastPass import, choose *Generic CSV* and paste from the clipboard.
