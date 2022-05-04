n = int(input())
str_list = []
for i in range(n):
    str_list.append(input())


for i in range(len(str_list)):
    bonus = 0
    score = 0
    for j in range(len(str_list[i])):
        if str_list[i][j] == 'O':
            bonus += 1
            score = score + bonus
        else:
            bonus = 0

    print(score)
