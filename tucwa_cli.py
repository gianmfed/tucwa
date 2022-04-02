# to kill the app in background
# TASKKILL /F /IM pythonw.exe
import gigi
from sqlite3 import connect



# Connect time.db database
con = connect('time.db')
db = con.cursor()

tutto = db.execute('SELECT * FROM time_table')
listadate = tutto.fetchall()

for data in listadate:
    print(data[1] // 60)

con.close()

print(gigi.bobbi)