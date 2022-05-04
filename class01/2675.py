n = int(input())
result_list = []
for i in range(n):
    repeat_times, input_str = map(str, input().split())
    result = ''
    for j in range(len(input_str)):
        for k in range(int(repeat_times)):
            result += input_str[j]
    result_list.append(result)

for result in result_list:
    print(result)
