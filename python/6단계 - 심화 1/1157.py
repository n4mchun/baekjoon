st = input().upper()
count_dict = {}

for c in st:
    if count_dict.get(c) == None:
        count_dict[c]  = 1
    else:
        count_dict[c] += 1

most_alphabets = []
max_count = max(count_dict.values())

for alphabet, count in count_dict.items():
    if count == max_count:
        most_alphabets.append(alphabet)

if len(most_alphabets) > 1:
    print('?')
else:
    print(most_alphabets[0])