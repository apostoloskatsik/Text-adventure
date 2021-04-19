import colors
''''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(("76.181.145.53", 1234))
    dataReceived = s.recv(1024).decode()
    print(f"You are player, {dataReceived}")
    dataReceived2 = s.recv(1024).decode()
    print(dataReceived2)
except:
    #print(colors.gray + "Connection Refused, Playing Solo.")
    pass
    #exit()
'''
import game

#while True:
#dataSend = input("Data Here:")
#s.send(bytes(dataSend,"utf-8"))
