a, b = map(str, input().split())
a_list = list(a)
b_list = list(b)
a_list.reverse()
b_list.reverse()
ra = int(''.join(a_list))
rb = int(''.join(b_list))
if ra > rb:
    print(ra)
else:
    print(rb)
