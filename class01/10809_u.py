# a~z ASCII : 97~122
s = input()
result_list = []
for i in range(26):  # 알파벳의 개수는 26개이다
    try:  # 인덱스를 찾지 못했을때 발생하는 ValueError: substring not found을 -1로 예외 처리
        # chr(97) = 'a', chr(98) = 'b' ...
        result_list.append(s.index(chr(i+97)))
    except:
        result_list.append(-1)

for i in result_list:
    print(i, end=' ')
