from sys import stdin as s
s = open('./input.txt', 'rt')
n = int(s.readline().strip())

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # 리스트를 반으로 나누기
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    # 각 반씩 재귀적으로 병합 정렬 호출
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # 두 리스트를 합치기
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    # 두 리스트를 비교하면서 작은 값을 결과에 추가
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # 남은 요소들을 결과에 추가
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


for _ in range(n):
  aNum, bNum = list(map(int, s.readline().strip().split()))
  aList = list(map(int, s.readline().strip().split()))
  bList = list(map(int, s.readline().strip().split()))
  merge_sort(aList)
  merge_sort(bList)

  result = 0
  for aItem in aList:
    for bItem in bList:
      if aItem > bItem:
        result += 1
  print(result)