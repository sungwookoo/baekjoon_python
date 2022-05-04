str = input().upper()
none_dup_str = list(set(str))
cnt_list = []
for char in none_dup_str:
    cnt_list.append(str.count(char))
if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(none_dup_str[cnt_list.index(max(cnt_list))])
