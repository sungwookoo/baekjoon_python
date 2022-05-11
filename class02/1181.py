# 문자열 길이 순으로 정렬, 길이가 같으면 알파벳순
n = int(input())
input_list = []

for _ in range(n):
    input_list.append(input())

temp_set = set(input_list)
input_list = list(temp_set)

input_list = sorted(input_list, key=lambda x: (len(x), x))

for i in input_list:
    print(i)
