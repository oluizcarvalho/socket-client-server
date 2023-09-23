import socket

# socket.AF_UNIX - LOCAL
# socket.AF_INET - IPV4

# socket.SOCK_STREAM - TCP
# socket.SOCK_DGRAM - UDP

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

s.bind((host, port))
print("socket binded to %s" % port)

s.listen(5)
print("socket is listening")

conn, addr = s.accept()
print('Got connection from ', addr[0], '(', addr[1], ')')
print('Thank you for connecting')

while True:
    data = conn.recv(1024)
    if not data: break
    print("from connected user: " + str(data))
    conn.sendall(data)
conn.close()
