n = int(input())

cnt = 0
for i in range(n):
    used_list = []
    word = input()
    for c in word:
        if c in used_list and used_list[-1] != c:
            break
        else:
            used_list.append(c)
    else:
        cnt += 1
print(cnt)