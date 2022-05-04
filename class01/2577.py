input_list = []
for i in range(3):
    input_list.append(int(input()))
result = str(input_list[0] * input_list[1] * input_list[2])

for i in range(10):
    print(result.count(str(i)))
