import socket

from sockets.sockets_mod import Socket


class TetrisGame:

    def __init__(self, host: str, port: int):
        super().__init__()
        self._current_connection = Socket.create_client_socket(host, port)




# PYGAME STUFF:

    # K_LEFT:	1073741904
    # K_RIGHT:  1073741903
    # K_DOWN:	1073741905
    # K_UP:     1073741906



# adicionados métodos para os diferentes INPUTS do jogo

    def move_left(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741904, 10)
        return self._current_connection.receive_int(10)

    def move_right(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741903, 10)
        return self._current_connection.receive_int(10)

    def move_down(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741905, 10)
        return self._current_connection.receive_int(10)

    def move_up(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741906, 10)
        return self._current_connection.receive_int(10)


    def exit(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("exit")

    def connect(self):
        self._current_connection = socket.socket()



