f = open("27B_27138.txt").readlines()

def maxrast(clss):
    maxras = 0
    for i in range(3):
        for x,y in clss[i]:
            rast = 0
            for j in range(3):
                if i != j:
                    for x1,y1 in clss[j]:
                        rast += ((x1-x)**2+(y-y1)**2)**0.5
            if rast > maxras:
                maxras = rast
                xc = x
                yc = y
                        
    return xc+yc

    
cls1 = []
cls2 = []
cls3 = []

for i in f:
    x,y = i.replace(",",".").split()
    x,y = float(x),float(y)
    if x<-40 and x>-60 and  y > 10 and y<30:
        cls1.append([x,y])
    elif 20<x<40 and 10<y<30:
        cls2.append([x,y])
    elif 30<x<50 and -35<y<-20:
        cls3.append([x,y])

Q1 = max(cls1)
Q2 = maxrast([cls1,cls2,cls3])
print(abs(int(Q1[0]*10000)),abs(int(Q2*10000)))



