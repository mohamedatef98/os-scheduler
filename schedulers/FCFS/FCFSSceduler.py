from ..abstractions.Scheduler import Scheduler
from ...gantt_chart.gantt_chart import Gantt_Chart
class FCFSScheduler (Scheduler):
    def __init__(self, queue):
        self.queue = queue
        self.processing

    def schedule(self):
        counter = 0
        sorted_queue = sorted(self.queue.processes, key=lambda k: k.arrival)
        gantt_chart = Gantt_Chart()
        for queue_process in sorted_queue:
            for i in range(queue_process.time):
                gantt_chart.add(h  )
