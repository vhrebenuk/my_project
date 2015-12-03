import socket
from os import path
import matplotlib.pyplot as plt
from pyparsing import Word, Literal, nums
import ftplib

def progress():    #Процесс отправка графика на сервер
    def callback(block):
        callback.uploaded += len(block)
        print('Uploaded %d bytes' % callback.uploaded)
    callback.uploaded = 0
    return callback

def menu_for_graph(udata):     #Вариативное меню для программы
    if udata == "g":
        last_line = pars_data()
        makegraph(last_line)
    elif udata == "s":
        print("settings")

def pars_data():            #Парсинг файла с данными
    f = open("test.txt" ,'r')
    all_lines = f.readlines()
    last_line = []
    last_line.append(all_lines[-1])
    for item in last_line:
        item += item
    temperatura = (Word(nums + '+.') | Word(nums + '-.'))
    comma = (Literal(",") | Literal(";")).suppress()
    tem = (temperatura + comma)*5
    full_name_temperatura = Word(nums + '.').suppress() + Word(nums + ':').suppress() + tem # парсинг температуры
    vremenno_temp= full_name_temperatura.parseString(item)                                  # парсинг температуры
    full_name_date = Word(nums + '.')                                   # парсинг даты
    vremenno_date = full_name_date.parseString(item)                    # парсинг даты
    data_date = str(vremenno_date)                                      # парсинг даты
    data_temperatura = []                                                                   # парсинг температуры
    for item in vremenno_temp:                                                              # парсинг температуры
        item = float(item)                                                                  # парсинг температуры
        data_temperatura.append(item)                                                       # парсинг температуры
    f.close
    return data_temperatura

def makegraph(data_temperatura):                                        # делаем и сохраняем график 
    Y_10 = data_temperatura
    X = [1, 2, 3, 4, 5]
    line = plt.plot(X, Y_10, 'go:')
    plt.axis([1, 5, -40, 40])
    plt.xlabel(u'Room')
    plt.ylabel(u'Temperatura')
    plt.grid()
    print("График построен")
    plt.savefig("graphic.png", dpi = 250)
    ftp_send()

def ftp_send():                                         #Отправка графика на сервер
    host = "node0.net2ftp.ru"
    ftp_user = "grebenuk.viktor@gmail.com"
    ftp_password = "8b0aab38"
    filename = 'graphic.png'
    
    con = ftplib.FTP(host, ftp_user, ftp_password)
    con.storbinary("STOR "+ filename, open(filename, "rb"), 1024, progress())   # Передаем файл на сервер

def listen_serv():                                      #Слушаем на предмет команд контроллер умного дома
    conn, addr = sock.accept()
    print("Hello new user: ", addr[0])
    while True:
        data = conn.recv(1024)
        udata = data.decode("utf-8")
        menu_for_graph(udata)
        if not data:
            listen_serv()
    conn.close()
    
sock = socket.socket ()
sock.bind(("", 13330))
sock.listen(3)
listen_serv()



