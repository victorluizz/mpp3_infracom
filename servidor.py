import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 24883))
s.listen(1)
print("Aguardando conexão...")
sockete_servidor = []
enderecos = []
verificiacao = True
while verificiacao:
    for i in range(2):
        if (i == 0):    
            print("Esperando o primeiro cliente se conectar.")
        else:
            print("Esperando o segundo cliente se conectar.")
        conn, addr = s.accept()
        sockete_servidor.append(conn)
        enderecos.append(addr)
        print("Concetado em: {} {}".format(addr[0], addr[1]))
        if (i == 0):
            print("Primeiro cliente conectado.")
        else:
            print("Segundo cliente conectado.")
        
    sockete_servidor[1].sendto(bytes(f"{enderecos[0][1]}", 'utf-8'), enderecos[1])
    sockete_servidor[0].sendto(bytes(f"{enderecos[1][1]}", 'utf-8'), enderecos[0])
    sockete_servidor.clear()
    enderecos.clear()

s.close()
print("Fechando conexão...")