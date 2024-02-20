from sys import stdin as s
s = open('./input.txt', 'rt')
caseNum = int(s.readline())
result = [] # 최종 결과를 담아둘 배열에 해당함

def solution(stickerArray, n):
  firstMemo = [0 for _ in range(n)]
  secondMemo = [0 for _ in range(n)]
  firstMemo[0] = stickerArray[0][0]
  secondMemo[0] = stickerArray[1][0]
  for j in range(1, n):
    if j % 2 == 0:
      firstMemo[j] = firstMemo[j - 1] + stickerArray[0][j]
      secondMemo[j] = secondMemo[j - 1] + stickerArray[1][j]
    else:
      firstMemo[j] = firstMemo[j - 1] + stickerArray[1][j]
      secondMemo[j] = secondMemo[j - 1] + stickerArray[0][j]
  print(firstMemo)
  print(secondMemo)

for i in range(caseNum):
  arrayLength = int(s.readline())
  tmpStickerArray = [list(map(int, s.readline().strip().split())) for _ in range(2)]
  maxValue = solution(tmpStickerArray, arrayLength)
  # result.append(maxValue)

# 해당 풀이는 트정 열을 선택하지 않고도 최대값을 뽑아낼 수 있음을 간과한 것
