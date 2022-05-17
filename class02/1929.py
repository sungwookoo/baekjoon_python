from sys import stdin
# 소수 구하기
start, end = map(int, stdin.readline().split())

def is_prime(num):
    if num == 1:
        return False
    else:
        # 2부터 num의 제곱근(**0.5) 까지 검사 
        for i in range(2, int(num**0.5)+1):
            print(i)
            if num%i == 0:
                return False
        return True

for i in range(start, end+1):
    if is_prime(i):
        print(i)
        