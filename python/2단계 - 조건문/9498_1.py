table = {90: 'A', 80: 'B', 70: 'C', 60: 'D'}

score = int(input())
for key in table.keys():
    if score >= key:
        print(table[key])
        break
else:
    print('F')