# 좌표 정렬하기
n = int(input())
input_list = []
result = []
for _ in range(n):
    x, y = map(int, input().split())
    input_list.append((x, y))

print(input_list)

# 두 번째 원소(x[1])로 오름차순 정렬, 두 번째 원소(x[1])가 같은 경우 첫 번째 원소(x[0])로 오름차순 정렬
input_list.sort(key=lambda x: (x[1], x[0]))

for i in input_list:
    print(i[0], i[1])
