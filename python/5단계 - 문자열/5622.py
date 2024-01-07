table = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
st = input()

time = 0
for char in st:
    for key in table.keys():
        if char in key:
            time += table[key]
print(time)