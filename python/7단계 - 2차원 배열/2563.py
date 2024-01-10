paper = [[0]*100 for _ in range(100)]

n = int(input())
for _ in range(n):
    _x, _y = map(int, input().split())
    for x in range(_x, _x+10):
        for y in range(_y, _y+10):
            # if paper[x][y] == 0:
            paper[x][y] = 1

area = 0
for i in range(100):
    area += sum(paper[i])
print(area)