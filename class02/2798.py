# 블랙잭
from sys import stdin
n, m = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))
sum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                sum = max(sum, cards[i]+cards[j]+cards[k])

print(sum)
