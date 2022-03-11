
# 1 container: produces lyrics and stores them in SQL
# 1 container: stores lyrics in a database

import time
import logging  # the luxury version of print
from sqlalchemy import create_engine

conn = create_engine('postgres://postgres:titanic99@postgresdb:5432/gloria')
#                     dbtype     user     psw       host       port dbname
# here we use the *internal* host + port


conn.execute("""
   CREATE TABLE IF NOT EXISTS karaoke (
       singer VARCHAR(64),
       lyrics TEXT
   );

""")

while True:
    for line in open('iwillsurvive.txt'):
        
        logging.critical(line)  # goes to docker output immediately

        print("this is from print"+line)

        print(line) # !!! we don't see this (easily)
        time.sleep(1.0)