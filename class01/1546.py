n = int(input())
input_list = list(map(int, input().split()))
max_score = max(input_list)
sum = 0
for score in input_list:
    sum += score/max_score*100
print(sum/n)
