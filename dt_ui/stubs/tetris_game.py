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

    def get_shape(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("shape")
        return self._current_connection.receive_obj()

    def create_grid(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("grid")
        return self._current_connection.receive_obj()

    def get_locked_positions(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("getlocked")
        return self._current_connection.receive_obj()

    def set_locked_positions(self, locked_positions):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("setlocked")
        self._current_connection.send_obj(locked_positions)

    def valid_space(self, piece):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("valid")
        self._current_connection.send_obj(piece)
        return self._current_connection.receive_obj()

    def clear_rows(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("clear")
        return self._current_connection.receive_int(10)

    def convert_shape_format(self, current_piece):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("convert")
        self._current_connection.send_obj(current_piece)
        return self._current_connection.receive_obj()

    def check_lost(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("lost")
        return self._current_connection.receive_int(10)

    def exit(self):
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("exit")

    def connect(self):
        self._current_connection = socket.socket()



