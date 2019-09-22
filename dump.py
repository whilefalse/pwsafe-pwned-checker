import pypwsafev3
from pypwsafev3 import PWSafe3
import sys
import getpass

def quote(string):
    return '"%s"' % string.replace('"', '""')

path = sys.argv[1]
password = getpass.getpass("Password for %s: " % path)

safe = None
try:
    safe = PWSafe3(
            filename = path,
            password = password,
            mode = "R")
except pypwsafev3.errors.PasswordError:
    raise Exception("Invalid password")

print "url,type,username,password,hostname,extra,name,grouping"
for record in safe:
    record_data = [
            record['URL'],
            '',
            record['Username'],
            record['Password'],
            '',
            record['Notes'],
            record['Title'],
            '' if not record['Group'] else record['Group'][0]]
    record_data = map(quote, record_data)
    print(','.join(record_data))


