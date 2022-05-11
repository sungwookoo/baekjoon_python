# 영화감독 숌
# 666이 들어가는 n번째 작은 수를 출력
n = int(input())
num = 666
count = 0
while n:
    if "666" in str(num):
        n -= 1
    num += 1
print(num-1)
