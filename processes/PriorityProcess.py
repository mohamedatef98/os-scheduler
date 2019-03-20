from .NormalProcess import NormalProcess

class PriorityProcess(NormalProcess):

    def __init__(self, name, time, priority):
        NormalProcess.__init__(name, time)
        self.priority = priority
