def f(a,b):
    if a<b-100:
        return 0
    if a==b:
        return 1

    num1 = a%10
    num2 = a//10%10
    num3 = (a//10//10)*100+num1*10+num2
    
   
    if num2>num1:
        return f(a-3,b)+f(num3,b)
    else:
        return f(a-3,b)
print(f(1001,959)*f(959,902))
