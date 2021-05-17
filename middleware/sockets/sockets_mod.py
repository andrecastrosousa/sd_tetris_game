from socket import socket, timeout
from typing import Union

import sockets


class Socket:
    def __init__(self):
        self._current_connection = None

    @property
    def current_connection(self):
        return self._current_connection

    @current_connection.setter
    def current_connection(self, value):
        self._current_connection = value

    def accept(self) -> Union['Socket', None]:
        try:
            client_connection, _ = self._current_connection.accept()
            new_socket = Socket()
            new_socket.current_connection = client_connection
            return new_socket
        except timeout:
            return None

    @property
    def peer_add(self):
        return self._current_connection.getpeername()

    def receive_int(self, n_bytes: int) -> int:
        data = self._current_connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self, value: int, n_bytes: int) -> None:
        self._current_connection.send(value.to_bytes(n_bytes, byteorder='big', signed=True))

    def receive_str(self) -> str:
        n_bytes: int = self.receive_int(sockets.INT_SIZE)
        received: bytes = self._current_connection.recv(n_bytes)
        print(received.decode())
        return received.decode()

    def send_str(self, value: str) -> None:
        to_send: bytes = value.encode()
        self.send_int(len(to_send), sockets.INT_SIZE)
        self._current_connection.send(to_send)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def close(self):
        if self._current_connection is not None:
            self._current_connection.close()

    @staticmethod
    def create_server_socket(port: int, timeout: int = None) -> 'Socket':
        new_socket: socket = socket()
        new_socket.bind(('', port))
        new_socket.listen(1)
        new_socket.settimeout(timeout)

        socket_middleware = Socket()
        socket_middleware.current_connection = new_socket
        return socket_middleware

    @staticmethod
    def create_client_socket(host: str, port: int) -> 'Socket':
        new_socket: socket = socket()
        new_socket.connect((host, port))

        socket_middleware = Socket()
        socket_middleware.current_connection = new_socket
        return socket_middleware
