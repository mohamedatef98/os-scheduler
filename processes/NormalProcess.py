from .Process import Process

class NormalProcess(Process):

    def __init__(self, name, time):
        self.name = name
        self.time = time