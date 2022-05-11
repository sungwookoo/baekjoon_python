# 랜선 자르기
# k 개의 각자 다른 길이를 가진 랜선을 잘라 최대 길이의 랜선 n 개를 만들때 최대길이는?
k, n = map(int, input().split())

input_list = []

for i in range(k):
    input_list.append(int(input()))

min_length = 1  # 랜선의 최소 길이
max_length = max(input_list)  # 랜선의 최대 길이

while min_length <= max_length:  # 이분 탐색
    mid = (min_length + max_length) // 2
    count = 0  # 랜선을 자르는 횟수
    for i in input_list:
        count += i // mid

    if count >= n:  # 만들어야 할 랜선 수 보다 더 많이 잘린 경우
        min_length = mid + 1  # 최소길이를 mid+1로 설정
    else:  # 만들어야 할 랜선 수 보다 더 적게 잘린 경우
        max_length = mid - 1  # 최대길이를 mid-1로 설정

print(max_length)  # 만들어야 할 랜선 수에 딱 맞게 잘린 경우 출력
