n, m = map(int, input().split())
input_array = []
change_count = []

for _ in range(n):
    input_array.append(list(map(str, input())))

# n * m 보드에서 8 * 8 보드로 자를 수 있는 경우의 수는 n-7 * m-7
for i in range(n-7):
    for j in range(m-7):
        # W로 시작하는 보드일 경우 변경 횟수
        start_w = 0
        # B로 시작하는 보드일 경우 변경 횟수
        start_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # (k + 1) % 2 로 인덱스들의 합의 짝수/홀수 여부로 체크무늬 검사 가능
                # 인덱스 합이 짝수인 경우
                if(k + l) % 2 == 0:
                    # W로 시작하는 보드일 경우 합이 짝수인 인덱스는 W여야함
                    # 그래서 합이 짝수인 인덱스가 B일 경우 W로 바꿔야 하기 때문에 start_w 를 1 증가
                    if input_array[k][l] != 'W':
                        start_w += 1
                    # B로 시작하는 보드일 경우 합이 짝수인 인덱스는 B여야함
                    # 그래서 합이 짝수인 인덱스가 W일 경우 B로 바꿔야 하기 때문에 start_b 를 1 증가
                    if input_array[k][l] != 'B':
                        start_b += 1
                # 인덱스 합이 홀수인 경우
                else:
                    # W로 시작하는 보드일 경우 합이 홀수인 인덱스는 B여야함
                    # 그래서 합이 홀수인 인덱스가 W일 경우 B로 바꿔야 하기 때문에 start_w 를 1 증가
                    if input_array[k][l] != 'B':
                        start_w += 1
                    # B로 시작하는 보드일 경우 합이 홀수인 인덱스는 W여야함
                    # 그래서 합이 홀수인 인덱스가 B일 경우 W로 바꿔야 하기 때문에 start_b 를 1 증가
                    if input_array[k][l] != 'W':
                        start_b += 1
        # 8*8 보드로 자른 한 번의 과정이 끝나면 W,B로 시작한 체스판을 만드려고 색을 변경한 횟수를 저장
        change_count.append(start_w)
        change_count.append(start_b)

print(min(change_count))
