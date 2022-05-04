# 음계
# 1 2 3 4 5 6 7 8 ascending
# 8 7 6 5 4 3 2 1 descending
# 8 1 2 7 6 3 5 4 mixed
ascending = False
descending = False

input_list = list(map(int, input().split()))
if input_list[0] == 1:
    for i in range(7):
        if input_list[i+1]-input_list[i] != 1:
            print('mixed')
            ascending = False
            break
        else:
            ascending = True
elif input_list[0] == 8:
    for i in range(7):
        if input_list[i]-input_list[i+1] != 1:
            print('mixed')
            descending = False
            break
        else:
            descending = True
else:
    print('mixed')


if ascending is True:
    print('ascending')
if descending is True:
    print('descending')
