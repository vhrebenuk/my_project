import socket
from os import path
import matplotlib.pyplot as plt
from pyparsing import Word, Literal, nums

def listen_serv():
    conn, addr = sock.accept()
    print("Hello new user: ", addr[0])
    while True:
        data = conn.recv(1024)
        udata = data.decode("utf-8")
        print (udata)
        menu_for_graph(udata)
        if not data:
            break
    conn.close()

def menu_for_graph(udata):
    if udata == "g":
        last_line = pars_data()
        #list_y=[]
        makegraph(last_line)
        listen_serv()
    elif udata == "s":
        print("settings")

def pars_data():
    f = open("test.txt" ,'r')
    all_lines = f.readlines()
    last_line = []
    last_line.append(all_lines[-1])
    for item in last_line:
        item += item
    temperatura = (Word(nums + '+.') | Word(nums + '-.'))
    comma = (Literal(",") | Literal(";")).suppress()
    full_name = Word(nums + '.').suppress() + Word(nums + ':').suppress() + (temperatura + comma)*5
    vremenno= full_name.parseString(item)
    data_temperatura = []
    for item in vremenno:
        item = float(item)
        data_temperatura.append(item)
    print(data_temperatura)
    f.close
    return data_temperatura

def makegraph(list_y):
    print(list_y)
    Y_10 = list_y
    X = [1, 2, 3, 4, 5]
    line = plt.plot(X, Y_10, 'go:')
    plt.axis([1, 5, -40, 40])
    plt.xlabel(u'Room')
    plt.ylabel(u'Temperatura')
    plt.grid()
    print("График построен")
    plt.savefig("graphic.png", dpi = 250)        

    
sock = socket.socket ()
sock.bind(("", 13330))
sock.listen(3)
listen_serv()



