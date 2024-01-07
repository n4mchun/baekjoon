import string

s = input()

# for i in string.ascii_lowercase:
#     try:
#         print(s.index(i), end=' ')
#     except:
#         print(-1, end=' ')

for i in string.ascii_lowercase:
    for idx, x in enumerate(s):
        if x == i:
            print(idx, end=' ')
            break
    else:
        print(-1, end=' ')