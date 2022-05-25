# 최대공약수, 최소공배수
from math import gcd, lcm
from sys import stdin
n, m = map(int, stdin.readline().split())
print(gcd(n, m))
print(lcm(n, m))


# 직접구현 (유클리드 호제법)
def gcd2(n, m):
    while m > 0:
        n, m = m, n % m
    return n


def lcm2(n, m):
    return n * m // gcd2(n, m)
