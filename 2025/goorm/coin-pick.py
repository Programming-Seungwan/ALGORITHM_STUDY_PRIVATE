# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
coinArray = list(map(int, input().strip().split(" ")))

def kadanesAlgo(arr):
	max_sum = arr[0]
	current_sum = arr[0]

	for i in range(1, len(arr)):
		current_sum = max(arr[i], arr[i] + current_sum)
		max_sum = max(current_sum, max_sum)

	return max_sum

print(kadanesAlgo(coinArray))