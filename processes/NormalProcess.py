from .Process import Process

class NormalProcess(Process):

    def __init__(self, name, arrival, time):
        self.name = name
        self.arrival = arrival
        self.time = time