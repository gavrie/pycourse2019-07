import socket

PORT = 1234


def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(('0.0.0.0', PORT))
    s.listen(10)
    print(f"listening on :{PORT}")

    while True:
        (c, addr) = s.accept()
        print(f'>>> connection from {addr}')
        c.send(b'hello from server\n')

        while True:
            message = c.recv(1024)
            if not message:
                print(f'>>> {addr} is done')
                c.close()
                break

            print(f'>>> received message: {message}')
            c.send(b'You said: ' + message)


if __name__ == '__main__':
    serve()
