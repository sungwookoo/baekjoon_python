# 카드2
from collections import deque
from sys import stdin
n = int(stdin.readline())
que = deque()
for i in range(n):
    que.append(i+1)
    # 1 2 3 4 5 6
    # 3 4 5 6 2
    # 5 6 2 4
    # 2 4 6
    # 6 4
    # 4
for _ in range(len(que)-1):
    que.popleft()
    que.append(que.popleft())

print(que.popleft())
