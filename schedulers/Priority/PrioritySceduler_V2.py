from ..abstractions.Scheduler import Scheduler
from gantt_chart.gantt_chart import Gantt_Chart
from .sort_priority import sort_priority1,FCFS_sort_priority
import copy

class PriorityScheduler (Scheduler):

	def schedule(self ,preemptive):
	
				
		counter = 0
		queuCopy = copy.deepcopy(self.queue.processes)
		sorted_queue_processes = sorted(queuCopy, key=lambda k: k.arrival)
		gantt_chart = Gantt_Chart()
		
		while len(sorted_queue_processes) > 0:
			if(sorted_queue_processes[0].arrival > counter):
				gantt_chart.add(None)
				counter += 1
				continue
			
			pos = 0
			PIndex = 0;
			highestPriority = sorted_queue_processes[0].priority
			while pos < len(sorted_queue_processes):
				if(sorted_queue_processes[pos].arrival > counter):
					break
				if(sorted_queue_processes[pos].priority < highestPriority):
					highestPriority = sorted_queue_processes[pos].priority
					PIndex = pos
				pos += 1
				
			while sorted_queue_processes[PIndex].time > 0:
			
				if preemptive:
					interrupt = False
					for p in sorted_queue_processes:
						if p.arrival > counter:
							break
						if p.arrival == counter and p.priority < sorted_queue_processes[PIndex].priority:
							interrupt = True
					if  interrupt:
						break;
				
				#calculate avg waiting time for current time slice
				self.avgWait += self.getWaitingProcNum(sorted_queue_processes, counter)/len(self.queue.processes)
					
				gantt_chart.add(sorted_queue_processes[PIndex])
				sorted_queue_processes[PIndex].time -= 1
				counter += 1
				
			if sorted_queue_processes[PIndex].time <= 0:
				sorted_queue_processes.pop(PIndex)
		
		return gantt_chart

