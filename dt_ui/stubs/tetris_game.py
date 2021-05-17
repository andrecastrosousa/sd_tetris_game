import socket

from sockets.sockets_mod import Socket


class TetrisGame:

    def __init__(self, host: str, port: int):
        super().__init__()
        self._current_connection = Socket.create_client_socket(host, port)

    def move_left(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("right")
        return self._current_connection.receive_str()

    def exit(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("exit")

    def connect(self):
        self._current_connection = socket.socket()
