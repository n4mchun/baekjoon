sides = sorted(list(map(int, input().split())))
print(sides[0] + sides[1] + min(sides[2], sides[0]+sides[1]-1))