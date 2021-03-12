#start
from collections import Counter

n = int(input())

wordList = list()
for i in range(n):
    wordList.append(input())

wordCount = Counter(wordList)
wordCount = {k:str(v) for k, v in wordCount.items()}
print(len(wordCount))
print(' '.join(wordCount.values()))
#end