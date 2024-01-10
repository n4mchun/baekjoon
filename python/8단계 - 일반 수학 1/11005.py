num, system = map(int, input().split())

max_i = 0
while system**(max_i+1) <= num:
    max_i+=1

case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''
for i in range(max_i, -1, -1):
    x = num // system**i
    result += case[x]
    num -= x * system**i
print(result)