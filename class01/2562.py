﻿input_list = []
for i in range(9):
    input_list.append(int(input()))
print(max(input_list))
print(input_list.index(max(input_list))+1)
