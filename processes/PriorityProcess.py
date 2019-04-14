from .NormalProcess import NormalProcess

class PriorityProcess(NormalProcess):

    def __init__(self, name, arrival, time, priority):
        NormalProcess.__init__(self,name, arrival, time)
        self.priority = priority
