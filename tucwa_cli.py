# to kill the app in background
# TASKKILL /F /IM pythonw.exe

from sqlite3 import connect



# Connect time.db database
con = connect('time.db')
db = con.cursor()

tutto = db.execute('SELECT * FROM time_table ORDER BY date DESC LIMIT 7')
listadate = tutto.fetchall()

print(listadate[0])

for data in listadate:
    print(data[1] // 60)

con.close()

# variabile da altro file importato
#print(gigi.bobbi)