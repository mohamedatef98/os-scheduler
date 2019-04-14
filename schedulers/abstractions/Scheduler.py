class Scheduler:
	def __init__(self, queue):
		pass

	def schedule(self):
		pass

	def getWaitingProcNum(sorted_queue_processes, counter):
		waitingProcNum = 0;

		for p in sorted_queue_processes:
			if p.arrival > counter:
				break
			if p.arrival < counter:
				waitingProcNum++

		waitingProcNum-- #remove the current executing process
		return waitingProcNum