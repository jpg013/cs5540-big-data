import random
from enum import Enum

class FileModes(Enum):
    READ   = "r" # Opens file in read mode
    WRITE  = "w" # Opens file in write mode
    APPEND = "a" # Opens file in append mode
    CREATE = "x" # Opens file in create mode
    

    @classmethod
    def has_value(cls, value):
        return any(value == item for item in cls)

class FileHandle():
    def __init__(self, file_path, mode, bufsize=1):
        if not FileModes.has_value(mode):
            raise Exception("Cannot open file handle with invalid mode {0}".format(mode))

        self.handle = open(file_path, mode.value, buffering=bufsize) 

    def write(self,val):
        self.handle.write(val)