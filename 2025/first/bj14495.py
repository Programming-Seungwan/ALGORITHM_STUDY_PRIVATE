from sys import stdin as s

s = open("./input.txt", "rt")

# 처음 몇개는 그냥 박아넣어주기
# 아래부터 올라가면서 이미 있으면 가져다가 쓰고, 없다면 새로 계산해서 박아넣고.
n = int(s.readline().strip())

memo = [False] * 117
memo[1] = 1
memo[2] = 1
memo[3] = 1
memo[4] = 2

if (n >= 5):
  for i in range(5, n + 1):
    memo[i] = memo[i - 1] + memo[i -3]

print(memo[n])