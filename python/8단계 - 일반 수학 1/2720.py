T = int(input())

table = [25, 10, 5, 1]

for i in range(T):
    money = int(input())

    for x in table:
        print(money // x, end=' ')
        money -= money // x * x
    print()