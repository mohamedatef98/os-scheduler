from ..abstractions.Scheduler import Scheduler
from gantt_chart.gantt_chart import Gantt_Chart
from .sort_priority import sort_priority1,FCFS_sort_priority
import copy
class PriorityScheduler (Scheduler):
    def __init__(self, queue):
        self.queue = queue

   
    def schedule(self,preemptive):
        counter = 0
        k =0
        
        check = True
        subarraypriority = [];
        sorted_queue_processes = sorted(self.queue.processes, key=lambda k: k.arrival)
        gantt_chart = Gantt_Chart()
        # testing purpose structures =======================
        # quantum =[None]*len(sorted_queue_processes) ;
        # rem = [None]*len(sorted_queue_processes);
        # quantum = []
        # rem = []
        # testing purpose structures <===================end
        while len(sorted_queue_processes) > 0:
            if(sorted_queue_processes[0].arrival <= counter and preemptive==False):
                sort_priority1(counter,sorted_queue_processes)
               
                for i in range(sorted_queue_processes[0].time):
                    gantt_chart.add(sorted_queue_processes[0])
                    counter += 1
                sorted_queue_processes.pop(0)
            elif(sorted_queue_processes[0].arrival <= counter and preemptive==True): #needs another loop as for i in range(len(sorted_queue_processes)):
                                                                                     # as the upper depends on pop(0) <==============[DONE]
                iter1 = k                                        
                print("K = ",k,"counter = ",counter,"iter1 = ",iter1)
                
                if(counter>len(sorted_queue_processes)-1):
                    print("break is in the way!")
                    break;
                # ============================  sub-array update =======================
                while(sorted_queue_processes[k].arrival<=counter):
                    subarraypriority.append(sorted_queue_processes[k])
                    k+=1
                    print("no of tasks in priority sub-array = ",len(subarraypriority))
                    if(k>len(sorted_queue_processes)-1):
                        break
                 # ============================  sub-array update <===================== 
                sort_priority1(counter,subarraypriority)
                FCFS_sort_priority(subarraypriority)        # <========== MAY NOT BE USED 
                for i in range(len(subarraypriority)):
                    print("sub-array-prioority = ",subarraypriority[i].name)
                # ============================ sub-array update end<=====================
                # ================calculating quantum and reminder ======================
                #start = iter1
                
                print("K = ",k)
                for i in range(k-iter1):       #remember any quantum should be replaced with subarray[i].quantum same for rem
                    if(k>len(sorted_queue_processes)-1):
                        subarraypriority[i].quantum = 0                                                                          
                        subarraypriority[i].rem = subarraypriority[i].time                                            
                    elif(i==0):
                        subarraypriority[i].quantum = sorted_queue_processes[k].arrival - subarraypriority[i].arrival  
                        subarraypriority[i].rem = subarraypriority[i].time - subarraypriority[i].quantum                               
                        check =bool(1 if(subarraypriority[i].quantum+subarraypriority[i].rem == subarraypriority[i].time) else 0)
                        print("ckeck = ",check)
                        if(check==False):
                            subarraypriority[i].quantum = subarraypriority[i].time
                            subarraypriority[i].rem = 0                                                                                 
                    else:
                        print("another process in same time")
                        subarraypriority[i].quantum = 0                                                                            
                        subarraypriority[i].rem = subarraypriority[i].time                                             
                    counter+=1
                # ================calculating quantum and reminder end <======================

        #=========================== check sectio end ========================================
       
        # sort_priority1(counter,subarraypriority)
        # for i in range(len(subarraypriority)):
        #     print("sub-array-prioority = ",subarraypriority[i].name)
        for i in range(len(sorted_queue_processes)):
            print("for process = ",sorted_queue_processes[i].name," quantum = ",sorted_queue_processes[i].quantum)
            print("for process = ",sorted_queue_processes[i].name," rem = ",sorted_queue_processes[i].quantum)
        #=========================== check sectio end ========================================    

                #=======================  view section    =========================================
        clone_sorted_priority = sorted_queue_processes.copy()
        FCFS_sort_priority(clone_sorted_priority)
        for i in range(len(clone_sorted_priority)):
            print("clone_sorted = ",clone_sorted_priority[i].name)
        for i in range(len(sorted_queue_processes)):
            for j in range(clone_sorted_priority[i].quantum):
                gantt_chart.add(clone_sorted_priority[i])
                   # sorted_queue_processes.pop(0)
        
        for i in range(len(subarraypriority)):
            for j in range(subarraypriority[i].rem):
                gantt_chart.add(subarraypriority[i])
                #======================= view section end<=========================================

            else:
                gantt_chart.add(None)
                counter += 1
        return gantt_chart
