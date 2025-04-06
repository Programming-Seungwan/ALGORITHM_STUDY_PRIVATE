# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 구름이마다 언제 태어났고, 몇년차 구름인지를 알 수 있어야 함.
# 홀수 년도와 짝수 년도를 어떻게 구분할지?
# 기존에 있는 데이터를 어떻게 활용할지
import copy
user_input = int(input())
# 구름이에 대한 카운트임
class Cloud:
    def __init__(self, birth_year):
        self.birth_year = birth_year
        self.division_count = 0
        self.is_alive = True

cloudList = []



# 돌면서 살아 있는 애들만 걸러냄.
for i in range(1, user_input + 1):
	if i == 1:
		cloudList.append([1, 0, True])
		continue
	tmpCloudList = []

	for cloud in cloudList:

		if (cloud[2]):
			tmpCloudList.append([i, 0, True])
			cloud[1] += 1
			if (cloud[0] % 2 == 0 and cloud[1] == 3):
				cloud[2] = False
			if (cloud[0] % 2 != 0 and cloud[1] == 4):
				cloud[2] = False
	cloudList.extend(tmpCloudList)

count = 0
for element in cloudList:
	if element[2] == True:
		count +=1

print(count)