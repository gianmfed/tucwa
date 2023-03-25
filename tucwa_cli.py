# to kill the app in background
# TASKKILL /F /IM pythonw.exe

from sqlite3 import connect

# Function to convert seconds to HH:MM
def sec_to_hhmm(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes - hours * 60
    return f"{hours}:{minutes}"

# Connect time.db database
con = connect('time.db')
db = con.cursor()

last_seven_day = db.execute('SELECT * FROM time_table ORDER BY date DESC LIMIT 7')
listadate = last_seven_day.fetchall()

print(f'\nOggi: {sec_to_hhmm(listadate[0][1])}\n')

print('Ultima settimana:')
sum_average = 0
for data in listadate:
    sum_average += data[1] // 60
    print(f'Giorno: {data[0]}, {sec_to_hhmm(data[1])} o {data[1]} minuti')

print(f'\nMedia: {sec_to_hhmm((sum_average * 60) // 7)} o {sum_average // 7} minuti al giorno\n')
input()

con.close()

# variabile da altro file importato
#print(gigi.bobbi)
