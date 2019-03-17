import socket


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print('8888 is bind')
    sock.bind(('127.0.0.1', 8888))

    while True:
        print('endless cycle')
        result = sock.recv(1024)
        print('Some message', result.decode('utf-8'))