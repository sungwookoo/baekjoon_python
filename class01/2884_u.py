﻿h, m = map(int, input().split())  # 시,분을 각각 h,m으로 입력받는다.
rm = m-45  # 45분 전으로 알람을 맞춰야 하니 rm(result minute)을 입력받은 분(m) 에서 45를 뺀 값으로 저장한다.
rh = h  # rh(result hour)은 시간이 당겨져야 변화가 있으니 일단 선언만 해둔다.
if rm < 0:  # 입력받은 분(m)에서 45를 뺀 값이 음수일 경우에 시간을 당기므로 if 문을 건다.
    rh = h-1  # 한 시간을 당겨야 하니 rh를 1을 뺀다
    if rh < 0:  # 입력 받은 시간이 0시 일경우 음수 시간이 발생하므로 이는 23시로 받아야한다.
        rh = 24 + rh  # rh = 24 + (-1) = 23 이므로  23시가 된다.
    # 입력받은 분(m)에서 45를 뺀 값이 음수이므로 rm = 60 + rm(음수) = 60보다 작은 양수가 된다.
    rm = 60 + rm

print(rh, rm)