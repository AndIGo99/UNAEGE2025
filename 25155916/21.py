def f(s,i): #s - кол-во камней на начало хода, i - кол-во оставшихся ходов
    if i == 0: # последний ход
        if s<5110 and s*2 >= 5110: #прошлый игрок не победил, а текущий может
            return True 
        else:
            return False
    else:
        if i%2 == 0:
            if s<5110 and s*2 >= 5110: #прошлый игрок не победил, а текущий может
                return True 
            if f(s+1,i-1) or  f(s+4,i-1) or f(s*2,i-1):
                return True
            else:
                return False
        else:
            if f(s+1,i-1) and  f(s+4,i-1) and f(s*2,i-1):
                return True
            else:
                return False

for s in range(1,5110):
    if f(s,3):
        print(s)
    
