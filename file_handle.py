import random
import os
from enum import Enum

class FileModes(Enum):
    READ   = "r" # Opens file in read mode
    WRITE  = "w" # Opens file in write mode
    APPEND = "a+" # Opens file in append mode
    CREATE = "x" # Opens file in create mode
    

    @classmethod
    def has_value(cls, value):
        return any(value == item for item in cls)

class FileHandle():
    def __init__(self, file_path, mode, bufsize=1):
        if not FileModes.has_value(mode):
            raise Exception("Cannot open file handle with invalid mode {0}".format(mode))
        
        self.file_path = file_path
        self.mode = mode
        self.bufsize = bufsize

        self.open_file_handle()
        #print(mode.value)
        #print(file_path)
        # self.handle = open(file_path, mode.value, buffering=bufsize) 

    def open_file_handle(self):
        """opens a file handle safely by first checking for directory existence
        and creating dir structure first if needed."""
        directory = os.path.dirname(self.file_path)

        try:
            os.stat(directory)
        except:
            os.mkdir(directory)

        self.handle = open(self.file_path, self.mode.value, buffering=self.bufsize) 

    def write(self,val):
        self.handle.write(val)