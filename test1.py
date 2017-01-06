import psycopg2
import time
import Levenshtein_search

conn = psycopg2.connect("host='127.0.0.1' port='5432' dbname='benchmark' user='postgres' password=''")
cur = conn.cursor()
cur.execute("set schema 'public';")
query_word = "\"philippe the original\""
max_dist = 2
sqlquery = "select name from restaurant_nophone_training where levenshtein_less_equal(name, '" + query_word + "', " + str(max_dist) + ") <= " + str(max_dist) + ";"
print(sqlquery)
starttime = time.clock()
cur.execute(sqlquery)
results = cur.fetchall()
print(str(time.clock() - starttime) + " sec")
print(results)
print(" ")

print("Levenshtein_search algorithm:")
cur.execute("select name from restaurant_nophone_training")
names = cur.fetchall()
namelist = []
for name in names:
    namelist.append(name[0])
	
idx = Levenshtein_search.populate_wordset(-1,namelist)
starttime = time.clock()
results = Levenshtein_search.lookup(idx,query_word,max_dist)
print(str(time.clock() - starttime) + " sec")
print(results)

Levenshtein_search.clear_wordset(idx)
conn.close()