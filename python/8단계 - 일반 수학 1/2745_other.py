num, system = input().split()
num = ''.join(reversed(num))
system = int(system)

case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
for i in range(len(num)-1, -1, -1):
    result += case.index(num[i]) * system**i
print(result)