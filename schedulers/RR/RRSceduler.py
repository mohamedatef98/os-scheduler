from ..abstractions.Scheduler import Scheduler
from gantt_chart.gantt_chart import Gantt_Chart
from queue.queue import Queue
import copy


class RRScheduler (Scheduler):

	def schedule(self,process_Quantum_input , quantum_std):
		counter = 0
		#quantum_std = process_Quantum_input
		finished = False
		new_ip = False
		index = 0
		subarrayRR = []
		k = 0
		size_change = False
		queuCopy = copy.deepcopy(self.queue.processes)
		sorted_queue_processes = sorted(queuCopy, key=lambda k: k.arrival)	
		quantum =[None]*len(sorted_queue_processes)
		gantt_chart = Gantt_Chart()
		end = len(sorted_queue_processes)
		# ================= quantum init	 ========================
		for i in range(len(sorted_queue_processes)):
			quantum[i] = sorted_queue_processes[i].time
		# ================= quantum init end ========================
		while len(sorted_queue_processes) > 0:
			if(sorted_queue_processes[0].arrival <= counter):
				# ==================== updating sub-arrayRR	 ==============
				
				if(end != 0):
					while(sorted_queue_processes[k].arrival<=counter):
						subarrayRR.append(sorted_queue_processes[k])
						k+=1
						end -=1
						new_ip = True
						print("no of tasks in sub-arrayRR = ",len(subarrayRR))

						if(end<=0):
							break
					# ============= index overwrite ===================
					if(new_ip == True and counter > 0):
						if(size_change == False):
							index = old_index+1
						else:
							index = old_index
							size_change = False
						print("new_index = ",index)
						new_ip = False
				# ==================== updating sub-arrayRR end ==============

				# ======== calculating quantum	========================
				#for i in range(len(sorted_queue_processes)):
					# sorted_queue_processes[i].
				
					
					
					
				quantum[index] -= quantum_std
				print("quantum = ",quantum)
				if( quantum[index] <= 0 ):
					quantum[index] += quantum_std
					finished = True
				print("finished = ",finished)
				# ======== calculating quantum end ========================
				old_index = index

				# ============= view section	 ==============
				if(finished == True):
					for j in range(quantum[index]):
						#calculate avg waiting time for current time slice
						self.avgWait += self.getWaitingProcNum(sorted_queue_processes, counter)/len(self.queue.processes)
						gantt_chart.add(subarrayRR[index])
						counter += 1
				else:
					for j in range(quantum_std):
						#calculate avg waiting time for current time slice
						self.avgWait += self.getWaitingProcNum(sorted_queue_processes, counter)/len(self.queue.processes)
						gantt_chart.add(subarrayRR[index])
						counter += 1
				# ============= view section end ==============

				# ==============  index update	 =================
				if(finished == True):
					pop_index = index
					if(index == len(subarrayRR) -1):
						index = (index + 1)% len(subarrayRR)
					else:
						index = (index + 1)% len(subarrayRR) -1
					subarrayRR.pop(pop_index)
					#sorted_queue_processes.pop(pop_index)
					quantum.pop(pop_index)
					finished = False
					size_change = True
					print("no of tasks in sub-arrayRR = ",len(subarrayRR))
				else:
					index = (index + 1)% len(subarrayRR)
				
				print("index = ",index)
				# ==============   index update end =================
				if(len(subarrayRR)==0 and len(quantum)==0):
					break


			   
				# for i in range(len(sorted_queue_processes)):
				#	 for j in range(sorted_queue_processes[i].quantum):
				#		 gantt_chart.add(sorted_queue_processes[i])
				#		 counter += 1
				# sorted_queue_processes.pop(0)
			else:
				gantt_chart.add(None)
				counter += 1
		return gantt_chart

