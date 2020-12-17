L = [x for x in range(1,31)]

numb, count, posi, tmp= 0, 0, 0, 0
while numb < 15:
    while count < 9:
        if posi < len(L):
            count += 1
            posi += 1
        else:
            posi = 0
            tmp = numb
    numb += 1
    posi -= 1
    count = 0
    L.pop(posi)
    
print(L)
