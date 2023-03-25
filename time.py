### Program that records the time spent at
from time import sleep
from sqlite3 import connect
from datetime import date, timedelta, datetime

# Connect time.db database
con = connect('time.db')
db = con.cursor()

# Create TABLE time_table if not created
db.execute("CREATE TABLE IF NOT EXISTS time_table (date TEXT, seconds INTEGER)")

# Time variables
today = date.today()
DTIME = 60 # Updating time in seconds
addminutes = 0 # Today's time spent

# Check if same day, otherwise add date
sameday = db.execute("SELECT count(date) FROM time_table WHERE date=?", (today,))
sameday = sameday.fetchone()[0]
if not sameday:
    db.execute("INSERT INTO time_table (date, seconds) VALUES (?, 0)", (today,))
    con.commit()
else:
    addminutes = db.execute("SELECT seconds FROM time_table WHERE date=?", (today,)).fetchone()[0]

# Set to 0 seconds every day that the program was not executed
# Check if it is a new database
dbentries = db.execute("SELECT count(date) FROM time_table")
dbentries = dbentries.fetchone()[0]
if dbentries > 1: # If it is not a new database
    daybefore = today - timedelta(days=1)
    # First day, transformed in type date, not datetime
    firstday = db.execute("SELECT date FROM time_table ORDER BY date LIMIT 1")
    firstday = datetime.strptime(firstday.fetchone()[0], "%Y-%m-%d").date()
    while (daybefore != firstday):
        # Check if the program was used during that day
        dayused = db.execute("SELECT count(date) FROM time_table WHERE date=?", (daybefore,))
        dayused = dayused.fetchone()[0]
        if not dayused:
            db.execute("INSERT INTO time_table (date, seconds) VALUES (?, 0)", (daybefore,))
            con.commit()
        daybefore = daybefore - timedelta(days=1)

# Update execution time
while True:
    sleep(DTIME)
    addminutes += DTIME
    db.execute("UPDATE time_table SET seconds = ? WHERE date = ?", (addminutes, today)) 
    con.commit()