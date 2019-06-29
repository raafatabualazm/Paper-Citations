csv_file = open('twitter.csv')
freq = dict()
for line in csv_file:
    freq[line] = freq.get(line, 0) + 1
print(len(freq))

