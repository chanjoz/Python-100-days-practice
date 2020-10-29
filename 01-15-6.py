import random
verl = int(input("pls input the length of verification code: "))
verset = '0123456789abcdefghijklmnopqrstuvwxyz' \
         'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(verl):
    p = random.randint(0, len(verset)-1)
    print(verset[p], end='')