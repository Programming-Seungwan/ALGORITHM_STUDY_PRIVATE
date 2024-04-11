def solution(n, times):
    start = min(times)
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            people += mid // time

            if people >= n: # 같을 수도 있고 더 많을 수도 있으나 일단 나온다
                break
        if people >= n: # 우선 answer에 표기해놓고 end를 하나 줄이므로서 정답을 좁혀 나간다, 다시 작아지면 else에 걸려서 위로 좁히면서 올라가는 것이다
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
