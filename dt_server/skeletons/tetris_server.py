import socket
from sockets.sockets_mod import Socket

import game


class TetrisServer(Socket):
    def __init__(self, port: int, tetris_server: game.TetrisServer):
        super().__init__()
        self._port = port
        self._server = tetris_server

    def left(self) -> None:
        print("dentro do left")
        string = self._server.left()
        self.send_str(string)

    def right(self) -> None:
        print("dentro do right")
        string = self._server.right()
        self.send_str(string)

    # def rotate















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
        elif request_type == "exit":
            last_request = True
            keep_running = False
        return keep_running, last_request


