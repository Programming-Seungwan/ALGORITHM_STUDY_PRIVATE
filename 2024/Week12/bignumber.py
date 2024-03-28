def solution(numbers):
  numbersList = list(map(str, numbers))
  # 문자열로 바꾸고 비교를 진행한다. 아스키 코드 비교를 진행하는데, 길이 제한을 풀어주기 위한 조치
  numbersList.sort(key=lambda x: x*3, reverse=True)
  return str(int(''.join(numbersList)))



print(solution([6, 10, 2]))