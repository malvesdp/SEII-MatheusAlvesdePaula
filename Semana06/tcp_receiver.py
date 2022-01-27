import socket # importa a biblioteca socket

TCP_IP = "127.0.0.1" # ip do servidor
FILE_PORT = 5005 # porta do arquivo
DATA_PORT = 5006 # porta dos dados
timeout = 3 # tempo de esgotamento 
buf = 1024 # tamanho do buffer

sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # iniciando socket
sock_f.bind((TCP_IP, FILE_PORT)) # 
sock_f.listen(1) #

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # iniciando socket
sock_d.bind((TCP_IP, DATA_PORT)) #
sock_d.listen(1) #


while True:
    conn, addr = sock_f.accept()
    data = conn.recv(buf)
    if data:
        print "File name:", data # printa na tela nome do arquivo
        file_name = data.strip()

    f = open(file_name, 'wb') # abrindo arquivo

    conn, addr = sock_d.accept()
    while True:
        data = conn.recv(buf)
        if not data:
            break
        f.write(data) # escrevendo dados no arquivo

    print "%s Finish!" % file_name # imprime na tela o nome do arquivo que a escrita foi finalizada
    f.close() # fechando arquivo
