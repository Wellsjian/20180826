
import pymysql
import hashlib

SALT = "*/-&^%$#@!"
class Database:
    def __init__(self,
                 host = "localhost",
                 port = 3306,
                 user = "root",
                 passwd = "123456",
                 database = "dict",
                 charset = "utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.connect()

    def connect(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user = self.user,
                                  passwd = self.passwd,
                                  database = self.database,
                                  charset = self.charset)
    def create_cur(self):
        self.cur =self.db.cursor()
    def close(self):
        self.db.close()
    def register(self,name,passwd):
        sql = "select name from user where name = '%s'" %name
        self.cur.execute(sql)
        #在数据库中查找不必提交,只有写操作才需提交
        r = self.cur.fetchone()

        if r:
            return False
        else:
            hash = hashlib.md5((name + SALT).encode())
            hash.update(passwd.encode())
            passwd = hash.hexdigest()
            print(passwd)

            sql = "insert into user (name,password) values (%s,%s)"
            try:
                self.cur.execute(sql,[name,passwd])
                self.db.commit()
                # r = self.cur.fetchall()
                # print(r)
                return True
            except Exception:
                self.db.rollback()
                return False
    def log_in(self,name,passwd):
        hash = hashlib.md5((name + SALT).encode())
        hash.update(passwd.encode())
        passwd = hash.hexdigest()
        print(passwd)

        sql = "select * from user where name = '%s' and password = '%s'"%(name,passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        print(r)
        if r:
            return True











