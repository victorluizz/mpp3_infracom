import socket
from threading import Thread
import time
import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 24883))
recebendo_server2 = s.recv(1024).decode()

print(recebendo_server2)
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', int(recebendo_server2)))


contador_mensagens = 0

def contador(): #Função para contar as mensagem
    global contador_mensagens
    
    contador_mensagens +=1
    
    return contador_mensagens

def enviar_mensagens(s): #Função para enviar as mensagens
    while 1:
        msg = input("")
        s.sendall(bytes("Usuário: Victor Luiz", 'utf-8'))
        s.sendall(bytes(f"Mensagem: {msg}", 'utf-8'))
        s.sendall(bytes(f"\nMensagem nº: {contador()} \n{datetime.date.today()} \n{datetime.datetime.now().hour}:{datetime.datetime.now().minute}" , 'utf-8')) #Corrigi o erro que estava printando o número da mensagem junto com a mensagem
        print("Mensagem Enviada")

def receber_mensagens(s): #Função para receber as mensagens
    while 1:
        data = s.recv(1024).decode()
        print(data)

    
    
    
def main(s):
    envia_mensagens = Thread(target=enviar_mensagens, args=(s,))
    recebe_mensagens = Thread(target=receber_mensagens, args=(s,))

    envia_mensagens.start()
    recebe_mensagens.start()
    


main(s)


    
