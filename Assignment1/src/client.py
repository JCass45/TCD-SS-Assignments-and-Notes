class Client:
    def __init__(self, handle, join_id, socket):
        self.handle = handle
        self.join_id = join_id
        self.socket = socket
        self.port = socket.getsockname()[1]
        self.socket.serve_forever()

    def __str__(self):
        return self.join_id

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.join_id == other.join_id

        return False
