from sys import stdin as s
import math

s = open("./input.txt", "rt")

[n, m] = map(int, s.readline().strip().split())

def isPrimeNumber(startNum, endNum):
    sieve = [True] * (endNum + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(endNum)) + 1):
        if sieve[i]: # 이미 False가 되어있다면 제끼고 넘어간다.
            for j in range(i * i, endNum + 1, i):
                sieve[j] = False # 배수들을 모두 False로 만들어줌

    # startNum부터 endNum까지의 소수만 출력
    primes = [i for i in range(startNum, endNum + 1) if sieve[i]]
    return primes

# 소수 출력
primes = isPrimeNumber(n, m)
for prime in primes:
    print(prime)