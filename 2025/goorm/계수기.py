# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
maxArray = list(map(int, input().strip().split(' ')))
initialArary = list(map(int, input().strip().split(' ')))
clickCount = int(input())

# 특정 자리수가 넘어가면 그 왼쪽 꺼를 올리고 0으로 셋팅하면 됨.0 인덱스꺼가 이미 max[0]과 같으면 
def updateParent(maxArr, initArr, index):
	tmpValue = initArr[index] + 1
	if (tmpValue > maxArr[index]):
		if (index != 0):
			initArr[index] = 0
			initArr = updateParent(maxArr, initArr, index - 1)

	else:
		initArr[index] = tmpValue

	return initArr


for _ in range(clickCount):
	initialArary = updateParent(maxArray, initialArary, len(initialArary) - 1)

print(initialArary)