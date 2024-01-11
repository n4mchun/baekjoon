N = int(input())

hell_nums = [666]
num = hell_nums[-1] + 1
while len(hell_nums) < N:
    if '666' in str(num):
        hell_nums.append(num)
        num = hell_nums[-1] + 1
    else:
        num += 1
print(hell_nums[N-1])