from ..abstractions.Scheduler import Scheduler
from ...gantt_chart.gantt_chart import Gantt_Chart
class FCFSScheduler (Scheduler):
    def __init__(self, queue):
        self.queue = queue
        self.processing

    def schedule(self):
        counter = 0
        sorted_queue = sorted(self.queue.processes, key=lambda k: k['arrival_time'])
        gantt_chart = Gantt_Chart()
        while(sorted_queue.count() != 0):
            counter += 1
            if(counter - 1 == sorted_queue[0]['arrival_time']):
                for i in range(sorted_queue[0]['process'].time):
                    gantt_chart.add(sorted_queue[0])
                sorted_queue.pop(0)
