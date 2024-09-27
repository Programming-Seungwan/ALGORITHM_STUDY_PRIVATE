from collections import Counter
import sys

n = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(n)])

# 정렬
arr.sort()

# 최빈값 찾기 함수
def get_frequent_number(arr):
    # Counter를 사용하여 빈도수 계산
    frequency = Counter(arr)
    max_freq = max(frequency.values())
    
    # 최빈값을 모두 찾아서 정렬
    most_frequent = [num for num, freq in frequency.items() if freq == max_freq]
    most_frequent.sort()
    
    # 하나만 있다면 그 값, 여러 개라면 두 번째로 작은 값 반환
    return most_frequent[1] if len(most_frequent) > 1 else most_frequent[0]

# 산술평균
mean = round(sum(arr) / n)
if mean == -0:  # -0 처리
    mean = 0

# 중앙값
median = arr[n // 2]

# 최빈값
mode = get_frequent_number(arr)

# 범위
range_value = arr[-1] - arr[0]

# 결과 출력
print(mean)
print(median)
print(mode)
print(range_value)
