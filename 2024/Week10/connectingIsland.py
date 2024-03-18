def solution(n, costs):
    answer = 0
    memo = [False for _ in range(n)]
    sortedCosts = sorted(costs, key=lambda x: x[2])
    # 새로 들어오는 것이 이미 있는 거면 pass
    for cost in sortedCosts:
        firstIsland, secondIsland, connectingCost = cost
        if memo[firstIsland] == True and memo[secondIsland] == True: continue
        if memo[firstIsland] == False or memo[secondIsland] == False:
            memo[firstIsland] = True
            memo[secondIsland] = True
            answer += connectingCost
            break

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

# 3번째 원소를 기준으로 오름차순 정렬



