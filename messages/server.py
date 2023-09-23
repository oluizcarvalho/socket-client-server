import socket


# socket.AF_UNIX - LOCAL
# socket.AF_INET - IPV4

# socket.SOCK_STREAM - TCP
# socket.SOCK_DGRAM - UDP

def server_program():
    host = socket.gethostname()
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()
