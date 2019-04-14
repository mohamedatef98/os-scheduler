from ..abstractions.Scheduler import Scheduler
from gantt_chart.gantt_chart import Gantt_Chart

class FCFSScheduler (Scheduler):

    def schedule(self):
        counter = 0
        sorted_queue_processes = sorted(self.queue.processes, key=lambda k: k.arrival)
        gantt_chart = Gantt_Chart()
        while len(sorted_queue_processes) > 0:
            if(sorted_queue_processes[0].arrival <= counter):
                for i in range(sorted_queue_processes[0].time):
                    #calculate avg waiting time for current time slice
                    self.avgWait += self.getWaitingProcNum(sorted_queue_processes, counter)/len(self.queue.processes)
                    gantt_chart.add(sorted_queue_processes[0])
                    counter += 1
                sorted_queue_processes.pop(0)
            else:
                gantt_chart.add(None)
                counter += 1
        return gantt_chart

