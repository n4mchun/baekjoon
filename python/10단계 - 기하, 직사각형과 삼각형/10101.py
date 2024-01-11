angles = [int(input()) for _ in range(3)]

if angles[0] == angles[1] == angles[2] == 60:
    print('Equilateral')
elif sum(angles) == 180:
    if angles[0] == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')