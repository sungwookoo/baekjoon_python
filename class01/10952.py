﻿while True:
    try:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
    except:
        break
    print(A+B)