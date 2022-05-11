# 팰린드롬수 : 거꾸로 읽어도 같은 수
input_list = []
result_list = []
while(True):
    num = input()
    if num == '0':
        break
    input_list.append(num)

for i in input_list:
    back = i[-(len(i)//2):]
    front = i[(len(i)//2)-1::-1]
    result_list.append('yes') if back == front else result_list.append('no')


for i in result_list:
    print(i)
