class Queue:
    def __init__(self):
        self.processes = []

    def addProcess(self, process):
        self.processes.append(process)