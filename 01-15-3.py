from random import randint

"""
find out all the Narcissus number
"""
for i in range(100, 1000):
    j = i // 100
    k = i % 100 // 10
    li = i % 100 % 10
    if i == j ** 3 + k ** 3 + li ** 3:
        print(i, end=" ")
print("are Narcissustic numbers")

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

"""
Puzzle for 100unit/100chick
"""
x = 200 // 14
for i in range(x, 0, -1):
    if (200 - 14 * i) % 8 == 0:
        j = (200 - 14 * i) / 8
        k = (100 - 5 * i - 3 * j) * 3
        print("100 unit can buy %d cock, %d ham and %d chicken"
              % (i, j, k))

"""
CRAPS gamble
"""
money = 1000
while money > 0:
    bet = int(input("pls input this round bet: "))
    if bet <= money:
        toss = randint(1, 6) + randint(1, 6)
        print("the toss is %d" % toss)
        if toss == 7 or toss == 11:
            money += bet
            print("player win, total balance up to %d" % money)
        elif toss == 2 or toss == 3 or toss == 12:
            money -= bet
            print("player lose, total balance down to %d" % money)
        else:
            while True:
                toss2 = randint(1, 6) + randint(1, 6)
                print("the toss is %d" % toss2)
                if toss2 == toss:
                    money += bet
                    print("player win, total balance up to %d" % money)
                    break
                elif toss2 == 7:
                    money -= bet
                    print("player lose, total balance down to %d" % money)
                    break
    else:
        print("You don't have enough balance")
print("You are out of balance")
