from sys import stdin as s
s = open('./input.txt', 'rt')
n = int(s.readline().strip())
classList = []
for _ in range(n):
  classList.append(list(map(int, s.readline().strip().split())))
classList.sort()
startTime, endTime = classList[0]
classCount = 1

for i in range(2, n):
  newStartTime, newEndTime = classList[i]
  if newStartTime < endTime:
    if newEndTime < endTime:
      endTime = newEndTime
      continue
    else:
      continue
  else:
    classCount += 1
    startTime = newStartTime
    endTime = newEndTime

print(classCount)