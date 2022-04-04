# to kill the app in background
# TASKKILL /F /IM pythonw.exe

from sqlite3 import connect



# Connect time.db database
con = connect('time.db')
db = con.cursor()

last_seven_day = db.execute('SELECT * FROM time_table ORDER BY date DESC LIMIT 7')
listadate = last_seven_day.fetchall()

print(f'\nOggi: {listadate[0][1] // 60} minuti\n')

print('Ultima settimana:')
sum_average = 0
for data in listadate:
    sum_average += data[1] // 60
    print(f'Giorno: {data[0]}, {data[1] // 60} minuti')

print(f'\nMedia: {sum_average // 7} minuti al giorno\n')

con.close()

# variabile da altro file importato
#print(gigi.bobbi)