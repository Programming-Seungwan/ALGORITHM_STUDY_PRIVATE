from sys import stdin as s

s = open("./input.txt", "rt")

# 슬라이딩 윈도우 알고리즘 문제임.
# 종료 조건을 명확하게 설정하는 것이 중요해보임.
# ending의 시작점부터 마지막까지를 결정하는 것이 중요함.
# ending의 시작점 : 0 + (간격 - 1)
# ending의 끝점 : 전체 배열의 길이 - 1

[n, k] = list(map(int, s.readline().strip().split(' ')))
temperatureList = list(map(int, s.readline().strip().split(' ')))
tmpSum = sum(temperatureList[0 : k])
maxSum = tmpSum


for i in range(k, len(temperatureList)):
  tmpSum = tmpSum - temperatureList[i - k] + temperatureList[i]
  if (tmpSum >= maxSum):
    maxSum = tmpSum

print(maxSum)