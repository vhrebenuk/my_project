import socket
from os import path
import matplotlib.pyplot as plt
from pyparsing import Word, Literal, nums
import ftplib

def ftp_send():   #Отправка графика на сервер
    host = "ftp.ex.ru"
    ftp_user = "root"
    ftp_password = "python"
    filename = "picture.png"
 
    con = ftplib.FTP(host, ftp_user, ftp_password)
    f = open(filename, "rb")
    send = con.storbinary("STOR "+ filename, f)

    con.close

def listen_serv():       
    conn, addr = sock.accept()
    print("Hello new user: ", addr[0])
    while True:
        data = conn.recv(1024)
        udata = data.decode("utf-8")
        menu_for_graph(udata)
        if not data:
            break
    conn.close()

def menu_for_graph(udata):
    if udata == "g":
        last_line = pars_data()
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
    tem = (temperatura + comma)*5
    full_name_temperatura = Word(nums + '.').suppress() + Word(nums + ':').suppress() + tem # temperature
    vremenno_temp= full_name_temperatura.parseString(item)                                  # temperature
    full_name_date = Word(nums + '.')                                   # date
    vremenno_date = full_name_date.parseString(item)                    # date
    data_date = str(vremenno_date)
    data_temperatura = []
    for item in vremenno_temp:
        item = float(item)
        data_temperatura.append(item)
    f.close
    return data_temperatura

def makegraph(data_temperatura):
    Y_10 = data_temperatura
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



