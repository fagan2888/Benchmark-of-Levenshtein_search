import psycopg2

conn = psycopg2.connect("host='127.0.0.1' port='5432' dbname='benchmark' user='postgres' password=''")
cur = conn.cursor()
cur.execute("""set schema 'public';""")

f = open('restaurant-nophone-training.csv','r')
f.readline() #skip the first line
cur.execute("select * from restaurant_nophone_training;")
print(cur.fetchall())
cur.copy_from(f, '"restaurant_nophone_training"', sep=',')

conn.commit()
conn.close()