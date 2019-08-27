
from socket import *
from select import select

HOST = "0.0.0.0."
PORT = 22222
ADDR = (HOST,PORT)

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

rlist = [sockfd]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is sockfd:
            connfd ,addr = r.accept()
            print("Connect from the port %d" %PORT)
            rlist.append(connfd)
        elif r is connfd:
            data = connfd.recv(1024)
            if not data:
                r.close()
                rlist.remove(r)
                continue
            print("Receive",data.decode())
            wlist.append(r)
    for w in ws:
        if w is connfd:
            w.send(b"ok")
            wlist.remove(w)
