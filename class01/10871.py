n, x = map(int, input().split())
input_list = list(map(int, input().split()))
for i in input_list:
    if(i < x):
        print(i, end=' ')
