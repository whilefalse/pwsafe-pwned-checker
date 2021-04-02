# pwsafe-pwned-checker

A tool to check the haveibeenpwned list of pwned passwords against a pwsafe3 password safe.

## Usage

First you need to download the list of haveibeenpwned pwned passwords from here https://haveibeenpwned.com/Passwords, and unzip it (the SHA1 version).

Then run:

    pip install -r requirements.txt
    python check.py <path-to-pwned-passwords.txt> <path-to-db.pwsafe3>
