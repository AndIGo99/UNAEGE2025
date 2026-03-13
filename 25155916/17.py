f = [int(x) for x in open("17 (4).txt")]

max2 = max([x for x in f if abs(x)%10 == 3 and 10<=abs(x)<100])

arr = []
for i in range(len(f)-1):
    u1 = 100<=abs(f[i])<1000
    u2 = 100<=abs(f[i+1])<1000
    if u1+u2 == 1 and str(abs(f[i]))[0] in "02468" and str(abs(f[i+1]))[0] in "02468":
        arr.append(f[i]+f[i+1])
print(min(arr),len(arr))
