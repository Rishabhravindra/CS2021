import math 
alist = [116.1,	115.7,	114.7,	115.1,	115.6]

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


dev = [28.9 -30.9 ,49.3-30.9 , 30.7-30.9 , 28.3 -30.9,28.4 -30.9, 25.4 -30.9, 33.7 -30.9 ,29.2 -30.9 ,23.6 -30.9 , 31.5-30.9
]

sum = 0

for e in dev:
	sum += e*e
ans  = math.sqrt(sum/(len(dev)))
print (ans)
selectionSort(dev)
print(dev)


