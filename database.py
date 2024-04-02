import psycopg2

con = psycopg2.connect(host="localhost",
                       database="jpadata",
                       user="postgres",
                       password="Alisha@83")
cur = con.cursor()
cur.execute("select id,name from person")
rows = cur.fetchall()
for r in rows:
    con.close()
