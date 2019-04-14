def sort_priority1(counter,sorted_queue_processes=[]):
    for i in range(len(sorted_queue_processes)-1):
        j=i+1
        for j in range(len(sorted_queue_processes)-1):
            if(sorted_queue_processes[j].time>=sorted_queue_processes[j+1].time and sorted_queue_processes[j].arrival < counter):
                temp = sorted_queue_processes[j];
                sorted_queue_processes[j]=sorted_queue_processes[j+1];
                sorted_queue_processes[j+1]=temp;
    return sorted_queue_processes

def FCFS_sort_priority(sorted_queue_processes=[]):
    for j in range(len(sorted_queue_processes)-1):
        if(sorted_queue_processes[j].arrival==sorted_queue_processes[j+1].arrival and sorted_queue_processes[j].time>sorted_queue_processes[j+1].time):
            temp = sorted_queue_processes[j];
            sorted_queue_processes[j]=sorted_queue_processes[j+1];
            sorted_queue_processes[j+1]=temp;
    return sorted_queue_processes



    

# processes = [12,3,4,5,6,3,-4]
# sort_priority(processes)       