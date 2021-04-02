import pypwsafev3
from pypwsafev3 import PWSafe3
import sys
import getpass
import hashlib

pwned_passwords_path = sys.argv[1]
pwsafe_path = sys.argv[2]
master_password = getpass.getpass("Password for %s: " % pwsafe_path)

safe = None
try:
    safe = PWSafe3(
            filename = pwsafe_path,
            password = master_password,
            mode = "R")
except pypwsafev3.errors.PasswordError:
    raise Exception("Invalid password")

print("Found", len(safe), "records")
passwords = {}
for record in safe:
    pwdsha = hashlib.sha1(record['Password'].encode()).hexdigest().upper()
    passwords[pwdsha] = (record['Title'], 0)

i = 0
with open(pwned_passwords_path, 'r') as f:
    while(True):
        line = f.readline()
        if not line:
            break

        i+=1
        if i % 1000000 == 0:
            print(i)

        [sha, count] = line.split(':')
        if sha in passwords:
            (title, existing_count) = passwords[sha]
            passwords[sha] = (title, existing_count + int(count))
            print("Found!! %s (%s)" % (title, int(count)))




