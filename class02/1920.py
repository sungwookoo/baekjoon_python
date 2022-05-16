# 수 찾기
from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())


# 이분 탐색
def binary_search(start, end, target, N):

    # 타겟을 찾지 못했을 경우 : 탐색 실패 (0)
    if start > end:
        return 0
    mid = (start + end) // 2

    # 타겟과 리스트 중간 값이 같을 경우 : 탐색 성공 (1)
    if N[mid] == target:
        return 1

    # 타겟이 리스트의 중간 값보다 작을 경우 : 반으로 잘라 왼쪽 재탐색
    elif N[mid] > target:
        return binary_search(start, mid-1, target, N)

    # 타겟이 리스트의 중간 값보다 클 경우 : 반으로 잘라 오른쪽 재탐색
    else:
        return binary_search(mid+1, end, target, N)


for target in M:
    start = 0
    end = len(N) - 1
    print(binary_search(start, end, target, N))
