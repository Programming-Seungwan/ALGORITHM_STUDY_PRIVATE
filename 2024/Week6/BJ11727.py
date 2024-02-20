from sys import stdin as s
#s = open('./input.txt', 'rt')
n = int(s.readline())

memo = [0 for _ in range(1001)]

memo[1] = 1
memo[2] = 3

for i in range(3, n + 1):
  memo[i] = memo[i - 1] + memo[i - 2] * 2
print(memo[n] % 10007)
