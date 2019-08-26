from threading import Thread,Lock
from time import *

class Account:
    def __init__(self,id,balance,lock):
        self.id = id
        self.balance = balance
        self.lock = lock


    #取钱
    def withdraw(self,amount):
        self.balance -= amount
     #存钱
    def deposit(self,amount):
        self.balance += amount
    #查看
    def get_balance(self):
        return self.balance

#创建用户

Tom = Account("Tom",5000,Lock())
Alex = Account("Alex",8000,Lock())

#转账函数

def transport(from1,to,amount):
    if from1.lock.acquire():
        from1.withdraw(amount)
        sleep(0.5)
        if to.lock.acquire():
            to.deposit(amount)
            to.lock.release()
        from1.lock.release()
    print("%s给%s转账完成"%(from1.id,to.id))
t = Thread(target=transport,args=(Tom,Alex,2000))
t1 = Thread(target=transport,args=(Alex,Tom,2000))

t.start()
t1.start()

t.join()
t1.join()