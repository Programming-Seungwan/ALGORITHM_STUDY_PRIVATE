# 나의 풀이
def solution(id_list, report, k):
    answer = []
    dataDictionary = {} # 자료를 담을 딕셔너리에 해당
    for id in id_list:
        dataDictionary[id] = {}
        dataDictionary[id]["count"] = 0 # 본인이 몇번 신고 당했는지를 의미함
        dataDictionary[id]["target"] = [] # 본인이 누구를 신고했는지를 의미하는 배열에 해당

    for reportData in report:
        # 아직 신고하지 않았으면 추가하고 신고했으면 뺀다
        refinedReportData = reportData.split(" ")
        fromPerson = refinedReportData[0]
        toPerson = refinedReportData[1]
        if toPerson in dataDictionary[fromPerson]["target"]:
            continue
        else:
            dataDictionary[fromPerson]["target"].append(toPerson)
            dataDictionary[toPerson]["count"] += 1

    forbiddenUserList = []
    for id in id_list:
        if (dataDictionary[id]["count"] >= k):
            forbiddenUserList.append(id)
    for id in id_list:
        count = 0
        for forbiddenUser in forbiddenUserList:
            if forbiddenUser in dataDictionary[id]["target"]:
                count += 1
        answer.append(count)
    print(answer)


# 모범 답안

1
2
3
4
5
6
7
8
9
10
11
12
13
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list} # 각 신고당한 사람들의 딕셔너리 컴프리헨션

    for r in set(report): # 중복을 자동으로 제거해줄 수 있는 set 자료형을 이용
        reports[r.split()[1]] += 1 # 신고당한 횟수를 하나씩 늘려줌

    for r in set(report):
        if reports[r.split()[1]] >= k: # 신고당한 횟수가 기준 k보다 크면
            answer[id_list.index(r.split()[0])] += 1 # 그걸 신고한 놈은 1을 먹는 구조

    return answer

## 어떻게 저런 문제를 풀어내는가? 중복되는 집합은 set() 자료형을 이용해 제거해버림
## 일종의 자료구조 short cut을 활용해 직관성을 높임
## 각 사람들은 자신이 제대로 된 사용자를 신고했으면 1씩 먹어야 하므로 이 역시 set(report)를 이용해 순회하면서 기준치보다 높다면 증가시킴 : 신고자 + 피신고자가 colocate 된 것을 캐치함