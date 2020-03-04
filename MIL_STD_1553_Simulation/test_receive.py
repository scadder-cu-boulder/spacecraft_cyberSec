import socket

port = 2000
socket_variable = \
    socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
socket_variable.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
socket_variable.bind(("", port))
while True:
    data, addr = socket_variable.recvfrom(1024)
    print(data)