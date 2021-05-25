import socket
from sockets.sockets_mod import Socket
from game.Jogo import Jogo

import game


class TetrisServer(Socket):
    def __init__(self, port: int, jogo: game.Jogo):
        super().__init__()
        self._port = port
        self._server = jogo

    def left(self) -> None:
        print("dentro do left")
        input = self._server.left()
        self.send_str(input)

    def right(self) -> None:
        print("dentro do right")
        input = self._server.right()
        self.send_int(input, 10)

    def down(self) -> None:
        print("dentro do down")
        input = self._server.down()
        self.send_int(input, 10)

    def up(self) -> None:
        input = self._server.up()
        self.send_int(input, 10)

    def get_shape(self):
        shape = self._server.get_shape()
        self.send_obj(shape)

    def create_grid(self):
        grid = self._server.create_grid()
        self.send_obj(grid)

    def get_locked_positions(self):
        locked_positions = self._server.get_locked_positions()
        self.send_obj(locked_positions)

    def set_locked_positions(self, locked_positions):
        self._server.set_locked_positions(locked_positions)

    def valid_space(self, piece):
        valid_space = self._server.valid_space(piece)
        self.send_obj(valid_space)

    def clear_rows(self, grid):
        rows_cleared = self._server.clear_rows(grid)
        self.send_int(rows_cleared, 2)

    def convert_shape_format(self, current_piece):
        shape = self._server.convert_shape_format(current_piece)
        self.send_obj(shape)

    def check_lost(self):
        lost = self._server.check_lost()
        self.send_int(lost, 2)

    def run(self) -> None:
        current_socket = socket.socket()
        current_socket.bind(('', self._port))
        current_socket.listen(1)

        keep_running = True
        while keep_running:
            self._current_connection, address = current_socket.accept()
            print("Client ", address, " just connected!")
            with self._current_connection:
                last_request = False
                while not last_request:
                    keep_running, last_request = self.dispatch_request()
                print("Client ", address, " disconnect ")
        current_socket.close()
        print("server stopped")

    def dispatch_request(self) -> (bool, bool):
        request_type = self.receive_str()
        last_request = False
        keep_running = True
        if request_type == "left":
            self.left()
        elif request_type == "right":
            self.right()
        elif request_type == "shape":
            self.get_shape()
        elif request_type == "grid":
            self.create_grid()
        elif request_type == "getlocked":
            self.get_locked_positions()
        elif request_type == "setlocked":
            self.set_locked_positions(self.receive_obj())
        elif request_type == "valid":
            self.valid_space(self.receive_obj())
        elif request_type == "clear":
            self.clear_rows(self.receive_obj())
        elif request_type == "convert":
            self.convert_shape_format(self.receive_obj())
        elif request_type == "lost":
            self.check_lost()
        elif request_type == "exit":
            last_request = True
            keep_running = False
        return keep_running, last_request


