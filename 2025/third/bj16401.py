# 조카들에게 모두 같은 길이의 과자를 나누어 주어야 함
# 각 막대들의 길이는 다르고, 과자를 하나로 합칠 수는 없음. 최대한 긴 길이의 과자를 주어야 함
# M < N인 경우, 넉넉하므로 제일 M 번째로 큰 거로 고르면 다 만족시킬 수 있음
# M > N인 경우, 일단 쪼개야함. 반갈을 해서 줄여 나가면서 몫을 구해가면서 조카들의 숫자를 만족하는지 살펴보기

from sys import stdin as s
s = open('./input.txt', 'rt')

[M, N] = list(map(int, s.readline().strip().split()))
cookieList = list(map(int, s.readline().strip().split()))

cookieList.sort()

if M <= N:
  print(cookieList[-M])
else:
  startLength = cookieList[-1] // 2
  flag = False
  for i in range(startLength, 0, -1):
    count = 0
    for cookie in cookieList[::-1]:
      count += (cookie // i)
      if (count >= M):
        print(i)
        flag = True
        break
    if (flag == True):
      break
  if (flag == False):
    print(0)