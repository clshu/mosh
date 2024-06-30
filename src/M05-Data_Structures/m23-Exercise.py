from pprint import pprint

sentence = "This is a common interview question"

counts = dict()

for char in sentence:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

pprint(counts, width=1)

counts_sorted = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

pprint(counts_sorted[0])
