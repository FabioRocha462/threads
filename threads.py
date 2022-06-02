import threading as th,queue
import random as r
from unittest import result

list_number = [r.randint(1,100)for i in range(1000)]
print(len(list_number))
list1 = list_number[0:249]
list2 = list_number[250:499]
list3 = list_number[500:749]
list4 = list_number[750:999]
list_sum = []
def sumlist(lista,q):
    #print(sum(lista))
    list_sum.append(sum(lista))


    

print("Start \n")

t1 = th.Thread(target=sumlist,args=(list1,list_sum))
t2 = th.Thread(target=sumlist,args=(list2,list_sum))
t3 = th.Thread(target=sumlist,args=(list3,list_sum))
t4 = th.Thread(target=sumlist,args=(list4,list_sum))

t1.start()
t2.start()
t3.start()
t4.start()
print("soma total", sum(list_sum))




