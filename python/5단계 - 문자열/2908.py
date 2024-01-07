num1, num2 = input().split()
print(max(int(num1[::-1]), int(num2[::-1])))