# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Puerto de comunicacion
port = 9000 

#1.- Se conecta a traves de un socket al programa servidor (127.0.0.1 en el puerto 9000)
sock.connect(('127.0.0.1',port))

# Leemos los datos del servidor
data = sock.recv(4096)

#2.- Al recibir el mensaje de bienvenida del servidor lo imprime en pantalla
print(data.decode())

#3.- Se desconecta del servidor y cierra la conexion.
sock.close()
print("CONEXIONES CERRADAS")

