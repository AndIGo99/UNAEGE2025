from fnmatch import *

arr = [2]
for M in range(3,10000):
    f = 0
    for dels in arr:
        if dels**2 > M:
            break
        if M%dels == 0:
            f = 1
            break
        
    if f == 0:
        arr.append(M)


for N in range(13245,10**10,13245):
    if fnmatch(str(N),"43?9*12?"):
        for dels in range(1,int(N**0.5)+1):
            if N%dels == 0:
                dels2 = N/dels
                if 999<dels<10000 and dels in arr or 999<dels2<10000 and dels2 in arr:
                    print(N,N/13245)
                    break
                    
