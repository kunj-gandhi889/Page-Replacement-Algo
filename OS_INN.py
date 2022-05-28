# 20BCE073 --> Kunj Mayank Gandhi
# 2CS403 Operating System Innovative Assignment
from prettytable import PrettyTable
from colorama import Fore
table = PrettyTable()
try:
    print(Fore.LIGHTMAGENTA_EX+"<--------------- PAGE REPLACEMENT ALGORITHMS --------------->"+Fore.RESET)
    string = list(map(int,input("Enter Space Seperated Page Reference String : \n").split()))
    while(True):
        pf = int(input("Enter no. of page frame : "))
        if(pf<=0):
            print(Fore.RED+"Page Frame Must be Positive"+Fore.RESET)
        else:
            pf2 = pf + 1   # for belady's anomaly
            break
except ValueError:
    print(Fore.RED+"Invalid Format!"+Fore.RESET)
else:  
    print("\nPage Reference String :",string)
    print("No. of Page Frames :",pf)  

    # FIFO --> When a page needs to be replaced page in the front of the queue is selected for removal. 

    fault = {"FIFO":0,"BELADY":0,"OPTIMAL":0,"LRU":0}
    col = []
    for i in range(pf):
        col.append(f"F{i+1}")
    table.add_column("",col)
    print(Fore.GREEN+"\n<==== First In First Out (FIFO) ====>"+Fore.RESET)
    print(Fore.BLUE+"\n\t--> The page which is assigned the frame first will be replaced first.\n"+Fore.RESET)
    queue = []
    ind=0
    for page in string:
        if(len(queue)<pf and page not in queue):
            queue.append(page)
            fault["FIFO"]+=1
        elif(len(queue)==pf and page not in queue):  # then only need to replace
            queue[ind] = page
            ind+=1
            fault["FIFO"]+=1
            if(ind==pf):
                ind = 0
        copy = queue.copy()
        while(len(copy)<pf):
            copy.append("")
        table.add_column(f"{page}",copy)
    print(table)
    print("Total Page Fault :",fault["FIFO"])
    print("Total Page Hit :",len(string)-fault["FIFO"])
    print("Fault Ratio : %.3f"%((fault["FIFO"])/len(string)*100))
    print("Hit Ratio : %.3f"%((len(string)-fault["FIFO"])/len(string)*100))

    # checking for belady's anomaly 
    queue = [] ; ind = 0
    for page in string:
        if(len(queue)<pf2 and page not in queue):
            queue.append(page)
            fault["BELADY"]+=1
        elif(len(queue)==pf2 and page not in queue):
            queue[ind] = page
            ind+=1
            fault["BELADY"]+=1
            if(ind==pf2):
                ind = 0
    print(Fore.BLUE+"--> Belady's Anomaly : By Increasing No. of Page Frame , no. of Page Fault Increases"+Fore.RESET)
    print(f"Total Page Fault for {pf+1} Page Frame :",fault["BELADY"])
    if(fault["BELADY"]>fault["FIFO"]):
        print("Belady's Anomaly :",True)
    else:
        print("Belady's Anomaly :",False)

    # optimal --> pages are replaced which would not be used for the longest duration of time in the future. 

    table.clear()
    col = []
    for i in range(pf):
        col.append(f"F{i+1}")
    table.add_column("",col)
    print(Fore.GREEN+"\n<==== Optimal Page Replacement ====>"+Fore.RESET)
    print(Fore.BLUE+"\n\t--> Pages are replaced which would not be used for the longest duration of time in the future.\n"+Fore.RESET)
    queue = []
    ind = 0
    for page in string:
        ind+=1
        if(len(queue)<pf and page not in queue):
            queue.append(page)
            fault["OPTIMAL"]+=1
        elif(len(queue)==pf and page not in queue):  # need to replace
            fault["OPTIMAL"]+=1
            new = string[ind:]  # gives string right to it
            count=-1
            max = 0
            check = 0
            for j in queue:
                count+=1
                if(j not in new):
                    queue[count] = page
                    check = 1
                    break
            if(check == 0): 
                for j in queue:
                    if(max < new.index(j)):
                        max = new.index(j)
                val = new[max]
                for k in range(pf):
                    if(queue[k]==val):
                        queue[k] = page
        copy = queue.copy()
        while(len(copy)<pf):
            copy.append("")
        table.add_column(f"{page}",copy)
    print(table)
    print("Total Page Fault :",fault["OPTIMAL"])
    print("Total Page Hit :",len(string)-fault["OPTIMAL"])
    print("Fault Ratio : %.3f"%((fault["OPTIMAL"])/len(string)*100))
    print("Hit Ratio : %.3f"%((len(string)-fault["OPTIMAL"])/len(string)*100))

    # LRU --> page will be replaced which is not used recently in past (least recent).

    table.clear()
    col = []
    for i in range(pf):
        col.append(f"F{i+1}")
    table.add_column("",col)
    print(Fore.GREEN+"\n<==== Least Recently Used (LRU) ====>"+Fore.RESET)
    print(Fore.BLUE+"\n\t--> Page will be replaced which is not used recently in past (least recent).\n"+Fore.RESET)
    queue = []
    ind = 0
    for page in string:
        ind+=1
        if(len(queue)<pf and page not in queue):
            queue.append(page)
            fault["LRU"]+=1
        elif(len(queue)==pf and page not in queue):  # need to replace
            fault["LRU"]+=1
            new = string[:ind]  # gives string left to it
            new.reverse()   # just reverse of optimal
            count=-1  
            max = 0
            check = 0
            for j in queue:
                count+=1
                if(j not in new):
                    queue[count] = page
                    check = 1
                    break
            if(check == 0): 
                for j in queue:
                    if(max < new.index(j)):
                        max = new.index(j)
                val = new[max]
                for k in range(pf):
                    if(queue[k]==val):
                        queue[k] = page
        copy = queue.copy()
        while(len(copy)<pf):
            copy.append("")
        table.add_column(f"{page}",copy)
    print(table)
    print("Total Page Fault :",fault["LRU"])
    print("Total Page Hit :",len(string)-fault["LRU"])
    print("Fault Ratio : %.3f"%((fault["LRU"])/len(string)*100))
    print("Hit Ratio : %.3f"%((len(string)-fault["LRU"])/len(string)*100))

# Example --> 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
# for Belady anomaly --> 1 2 3 4 1 2 5 1 2 3 4 5