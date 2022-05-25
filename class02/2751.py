# 수 정렬하기 2
from sys import stdin
n = int(stdin.readline())
input_list = [i for i in range(10000)]
for _ in range(n):
    input_list.append(int(stdin.readline()))

input_list.sort()
for i in input_list:
    print(i)
