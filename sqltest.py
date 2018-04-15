
import MySQLdb as sql
import sys

try:
	injection = [ x for x in sys.argv[1:]]
	c = 0
	for i in injection:
		print(i, c)
		c += 1
except: pass

try:
	db = sql.connect(host="academic-mysql.cc.gatech.edu",
					 user="cs4400_team_26",
					 passwd="YFxUWSqD",
					 db="cs4400_team_26")
except Exception as e:
	print(e)

ATTRS = 'Name, ID, Street, Size, City, Zip, PropertyType, IsPublic, IsCommercial'

cursor = db.cursor()
# sql = "SELECT * FROM Visit"
sql = f"SELECT {ATTRS}, COUNT(Rating), AVG(Rating) AS ar FROM Property INNER JOIN \
		Visit ON ID=PropertyID GROUP BY Name ORDER BY ar DESC"
# sql = f"SELECT {ATTRS}, Rating FROM Property INNER JOIN Visit ON ID=PropertyID"
cursor.execute(sql)
data = cursor.fetchall()
# sql = f"SELECT Name, COUNT(Rating) FROM {data}"
# cursor.execute(sql)
# data = cursor.fetchall()
for x in data: print(x)
# print(data)