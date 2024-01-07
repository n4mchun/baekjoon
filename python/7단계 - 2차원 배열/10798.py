word_list = []

for i in range(5):
    word_list.append(input())
max_len = max([len(x) for x in word_list])

answer = ''
for i in range(max_len):
    for word in word_list:
        if len(word) > i:
            answer += word[i]
print(answer)