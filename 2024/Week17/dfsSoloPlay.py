def solution(cards):
    global cnt
    answers = [0]
    isChecked = [False for i in range(len(cards) + 1)]
    for i in range(1,len(cards) + 1):
        cnt = 1
        if isChecked[i] == False:
            isChecked[i] = True
            dfs(cards, i, isChecked)
            answers.append(cnt)
    tmp = sorted(answers, reverse = True)

    return tmp[0] * tmp[1]

def dfs(cards, n, isChecked):
    global cnt
    if isChecked[cards[n-1]] == False:
        isChecked[cards[n-1]] = True
        cnt += 1
        dfs(cards, cards[n-1], isChecked)



### 모범 답안
def solution(cards):
    answer = []
    for i in range(len(cards)): # 그냥 cards의 모든 요소를 죄다 순회
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1 # 없는 거면 추가해주고 i를 갱신해주기
        answer.append([] if sorted(tmp) in answer else sorted(tmp)) # 이미 넣은 집합이면 []를 넣고, 아직 안 넣은 것이면 정렬해서 넣어주기
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])
