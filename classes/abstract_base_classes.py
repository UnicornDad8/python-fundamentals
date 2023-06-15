from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# We inherit from ABC (abstract base class)
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # We anounce other classes inherited from this on are going to have
    # a read method but we don't need to provide the details of implementation
    # here in this class
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


# We need to redefine the read method on the Stream class otherwise this class
# Will also be an abstract class...
class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


stream = MemoryStream()
stream.read()
