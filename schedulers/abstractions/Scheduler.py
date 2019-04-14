class Scheduler:
	def __init__(self, queue):
		self.queue = queue
		self.avgWait = 0
		

	def schedule(self):
		pass

	def getWaitingProcNum(self,sorted_queue_processes, counter):
		waitingProcNum = 0;
		if(sorted_queue_processes[0].arrival > counter):
			return 0

		for p in sorted_queue_processes:
			if p.arrival > counter:
				break
			if p.arrival <= counter:
				waitingProcNum+=1

		waitingProcNum-=1 #remove the current executing process
		return waitingProcNum