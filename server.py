import socket
import threading


# socket.AF_UNIX - LOCAL
# socket.AF_INET - IPV4

# socket.SOCK_STREAM - TCP
# socket.SOCK_DGRAM - UDP

def on_new_client(clientsocket, addr):
    while True:
        data = clientsocket.recv(1024).decode()
        print(addr, ' >> ', data)
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        clientsocket.send(data.encode())
    clientsocket.close()


def server_program():
    host = socket.gethostname()
    port = 12347

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    print("socket binded to %s" % port)

    server_socket.listen(5)
    print("socket is listening")

    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        minha_thread = threading.Thread(target=on_new_client, args=(conn, address))
        minha_thread.start()
        minha_thread.join()
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    conn.close()


if __name__ == '__main__':
    server_program()
