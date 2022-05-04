n = int(input())
result_list = []
for i in range(n):
    input_list = list(map(int, input().split()))
    a = input_list[0]
    b = input_list[1]
    result_list.append(a+b)

for i in result_list:
    print(i)
