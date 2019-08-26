
import  pymysql
import re

obj = open("dict.txt")

db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     passwd = "123456",
                     database = "dict",
                     charset = "utf8")

cur = db.cursor()

sql = "insert into words(word,mean) values (%s,%s)"

try:
    for line in obj:
        data = re.findall(r"(\S+)\s+(.*)",line)[0]

        cur.execute(sql,data)
        db.commit()
except Exception as e:
    db.rollback()
    print(e)

else:
    cur.close()
    db.close()
