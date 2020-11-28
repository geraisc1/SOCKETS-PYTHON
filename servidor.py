# Importamos las librerias necesarias
import socket

# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9000 # Puerto de comunicacion

#1.- Abrir un socket que acepte conexiones en la ip local (127.0.0.1) en el puerto 9000
# IP y Puerto de conexion en una Tupla
sock.bind(('127.0.0.1',port)) 


#2.- El servidor queda a la espera de conexiones
print ("En espara de conexiones en el puerto ", port)
sock.listen(1)

# Cuando un cliente se conecte vamos a obtener la client_addr osea la direccion
# tambien vamos a obtener la con, osea la conexion que servira para enviar datos y recibir datos
con, client_addr =  sock.accept()

#3.- Cuando un cliente se conecta el servidor muestra un mensaje en la pantalla "CLIENTE CONECTADO"
print"CLIENTE CONECTADO"

#4.- El servidor envia un mensaje de texto al cliente a traves de la conexion "HOLA SOY EL SERVIDOR"
text = "Hola, soy el servidor!"

# Enviamos el texto al cliente que se conecta
con.send(text.encode()) 


# Cerramos la conexion
con.close() 

#5.- Al desconectarse un cliente el servidor muestra un mensaje "CLIENTE DESCONECTADO"
print"CLIENTE DESCONECTADO"

# Cerramos el socket
sock.close() 