import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#ragul70",
    database="worker"
)
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS details (id INT, regno INT, mobno INT)")
cur.execute("INSERT INTO details(id, regno, mobno) values(1, 71, 63)")
print(cur.rowcount)
