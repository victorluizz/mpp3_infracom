import socket
from threading import Thread
import random
import time
import datetime


portas_sorteadas = random.randint(1024, 30000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', portas_sorteadas))
s.connect(('localhost', 24883))
recebendo_server1 = s.recv(1024).decode()

print(recebendo_server1)

s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', portas_sorteadas))
s.listen(1)
print("Aguardando conexão...")
conn, addr = s.accept()

contador_mensagens = 0
def contador(): #Criei uma função para contar as mensagens enviadas pelo usuário
    global contador_mensagens
    
    contador_mensagens +=1
    
    return contador_mensagens

def enviar_mensagens(s): #Função para enviar mensagens
    while 1:
        msg = input("")
        s.sendall(bytes("Usuário: Daniel Queiroz", 'utf-8'))
        s.sendall(bytes(f"Mensagem: {msg}", 'utf-8'))
        s.sendall(bytes(f"\nMensagem nº: {contador()} \n{datetime.date.today()} \n{datetime.datetime.now().hour}:{datetime.datetime.now().minute}" , 'utf-8')) #Corrigi o erro que estava printando o número da mensagem junto com a mensagem
        print("Mensagem Enviada")
    
        
def receber_mensagens(s): #Função para receber mensagem
    while 1:
        data = s.recv(1024).decode()
        print(data)

def main(s):
    envia_mensagens = Thread(target=enviar_mensagens, args=(s,))
    recebe_mensagens = Thread(target=receber_mensagens, args=(s,))

    envia_mensagens.start()
    recebe_mensagens.start()
    
   

main(conn)



    
    
