import socket # importa a biblioteca socket
import sys # importa a biblioteca sys

TCP_IP = "127.0.0.1" # ip do servidor
FILE_PORT = 5005 # porta de arquivo
DATA_PORT = 5006 # porta dos dados
buf = 1024 # tamanho do buffer
file_name = sys.argv[1] # nome do arquivo

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # iniciando o socket
    sock.connect((TCP_IP, FILE_PORT)) # realizando conexão
    sock.send(file_name) # enviando nome do arquivo
    sock.close() # fechando o socket

    print "Sending %s ..." % file_name # printa na tela o nome do arquivo que está sendo enviado

    f = open(file_name, "rb") # abrindo arquivo
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # iniciando socket
    sock.connect((TCP_IP, DATA_PORT)) # realizando conexão
    data = f.read() # lendo os dados do arquivo
    sock.send(data) # enviando os dados do arquivo

finally:
    sock.close() # finalizando conexão
    f.close() # fechando arquivo

