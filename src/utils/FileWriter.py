from src.utils.Singleton import Singleton


class FileWriter(metaclass=Singleton):
    file = None

    def __init__(self, file_name='results.csv'):
        self.file_name = file_name

    def append(self, param):
        self.file = open(self.file_name, 'a')
        self.file.write(str(param) + '; ')
        self.file.close()

    def nl(self):
        self.file = open(self.file_name, 'a')
        self.file.write('\n')
        self.file.close()
