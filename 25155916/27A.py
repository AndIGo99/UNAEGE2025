f = open("27A_27138.txt").readlines()

def center(cls):
    minlen = 10**10
    for x,y in cls:
        summl = 0
        for x1,y1 in cls:
            summl += ((x1-x)**2+(y-y1)**2)**0.5
        if summl < minlen:
            minlen = summl
            xc = x
            yc = y
    return [xc,yc]        


    
cls1 = []
cls2 = []

for i in f:
    x,y = i.replace(",",".").split()
    x,y = float(x),float(y)
    if y > 0:
        cls1.append([x,y])
    else:
        cls2.append([x,y])

x1,y1 = center(cls1)
x2,y2 = center(cls2)
Sx = abs(x1-x2)
Sy = abs(y1-y2)
print(int(Sx*10000),int(Sy*10000))



