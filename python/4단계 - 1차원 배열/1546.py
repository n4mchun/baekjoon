n = int(input())
scores = list(map(int, input().split()))

new_scores = [x/max(scores)*100 for x in scores]
print(sum(new_scores) / n)