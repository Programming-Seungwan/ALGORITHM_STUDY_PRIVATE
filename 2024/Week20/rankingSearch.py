def solution(info, query):
    infoDataDic = {"cpp": {"frontend" : { "senior": { "chicken" : [], "pizza" : [] }, "junior": { "chicken" : [], "pizza" : [] } }, "backend": { "senior": { "chicken" : [], "pizza" : [] }, "junior": { "chicken" : [], "pizza" : [] } }}, "java": {"frontend" : { "senior": { "chicken" : [], "pizza" : [] }, "junior": { "chicken" : [], "pizza" : [] } }, "backend": { "senior": { "chicken" : [], "pizza" : [] }, "junior": { "chicken" : [], "pizza" : [] } }}, "python": {"frontend" : { "senior": { "chicken" : [], "pizza" : [] }, "junior": { "chicken" : [], "pizza" : [] } }, "backend": { "senior": { "chicken" : [], "pizza" : [] }, "junior": { "chicken" : [], "pizza" : [] } }}}

    answer = []

    for candidateInfo in info:
        cdInfoList = candidateInfo.split(" ")
        infoDataDic[cdInfoList[0]][cdInfoList[1]][cdInfoList[2]][cdInfoList[3]].append(int(cdInfoList[4]))

    for queryInfo in query:
        queryInfoList = queryInfo.split(" and ")
        food, grade = queryInfoList[3].split(" ")
        queryInfoList.pop()
        queryInfoList.append(food)
        queryInfoList.append(int(grade))
        result = 0

        wantLang = ['cpp','java', 'python'] if queryInfoList[0] == '-' else [queryInfoList[0]]
        wantPosition = ['frontend', 'backend'] if queryInfoList[1] == '-' else [queryInfoList[1]]
        wantYear = ['senior', 'junior'] if queryInfoList[2] == '-' else [queryInfoList[2]]
        wantFood = ['chicken', 'pizza'] if queryInfoList[3] == '-' else [queryInfoList[3]]
        wantScore = queryInfoList[4]
        for l in wantLang:
            for p in wantPosition:
                for y in wantYear:
                    for f in wantFood:
                        for score in infoDataDic[l][p][y][f]:
                            if score >= wantScore:
                                result += 1
        answer.append(result)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# 자료 구조 : 딕셔너리에 저장해야 빠름
# 언어 - 직군 - 경력 - 선호 음식의 구조로 저장하기
# 해당 풀이로는 문제는 풀리지만, 효율성 검사에서 에러가 발생함
