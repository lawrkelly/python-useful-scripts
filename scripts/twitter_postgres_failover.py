import os
import sys
import subprocess
import datetime
import time

datadir = "/Library/PostgreSQL/9.3/data"
email = "lawrkelly@gmail.com"



def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)


def start_pg():
    try:
        startup = 'sudo -S -u postgres /Library/PostgreSQL/9.3/bin/pg_ctl -U postgres start -D /Library/PostgreSQL/9.3/data'
        os.system(startup)

def write_fail():
            file = open('/Users/lkelly/Documents/database_check.txt','w')
            file.write(datetime.datetime.now().ctime())
            file.write('\n')
            file.write('Database restart failed\n')
            file.write('Database failover starting\n')
            file.close()

def write_success():
            file = open('/Users/lkelly/Documents/database_check.txt','w')
            file.write(datetime.datetime.now().ctime())
            file.write('\n')
            file.write('Database restarted successfully')
            file.close()

def check_postgres():
    try:
        status = subprocess.getoutput('sudo -u postgres pg_ctl status -D /Library/PostgreSQL/9.3/data', shell=True)
        if status in 'no server running':
            start_pg()
            time.sleep(10) # delays for 10 seconds.
        status = subprocess.getoutput('sudo -u postgres pg_ctl status -D /Library/PostgreSQL/9.3/data', shell=True)
        if status in 'no server running':
            write_fail()
            failover()
        else:
            write_success()
    finally:
        os.system('mutt -s \"database status \" -a /tmp/database_check.txt'  + email)

def failover():
    with open("/tmp/database_check.txt", "r") as db_check:
    searchlines = db_check.readlines()
    for i, line in enumerate(searchlines):
         if "failed" in line:
            os.system('repmgr -f repmgr/master/repmgr.conf --verbose master register')

            os.system('repmgr -f repmgr/master/repmgr.conf --verbose standby register')

def main():

    file = open('/Users/lkelly/Documents/database_failover.txt','w')
    file.write(datetime.datetime.now().ctime())
    check_postgres()

main()