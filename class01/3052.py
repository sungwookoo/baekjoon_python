input_list = []
for i in range(10):
    input_list.append(int(input()))

result_list = []
for num in input_list:
    result_list.append(num % 42)
    if(result_list.count(num % 42) > 1):
        result_list.remove(num % 42)

print(len(result_list))
