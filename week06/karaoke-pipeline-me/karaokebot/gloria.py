
# 1 container: produces lyrics and stores them in SQL
# 1 container: stores lyrics in a database

import time
import logging  # the luxury version of print
from sqlalchemy import create_engine


HOST = 'localhost'
PORT = '5433'
USERNAME = 'azadeh'
PASSWORD = '' 
DB = 'gloria'

#conn_mac = f'postgresql+psycopg2://{HOST}:{PORT}/{DB}'
#conn = create_engine(conn_mac)
conn = create_engine('postgresql://postgres:titanic99@postgresdb:5432/gloria')
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


"""

What do we need to write the song lines to Postgres from the Python script?

TODO:

- create/find a database
- check ports/hosts on docker ps -a
- what is the IP/hostname + port of the database?
  external: 0.0.0.0:5555
  psql -h 0.0.0.0 -p 5555 -U postgres

- specify the connection between containers (Dockerfile?)
- connect to the database with psql/pgadmin (for testing)
- connect to the database with SQLAlchemy
- create a table
- dump a user/text pair into the table
"""