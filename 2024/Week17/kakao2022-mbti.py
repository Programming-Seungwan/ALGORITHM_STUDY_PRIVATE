def solution(survey, choices):
    answer = ''
    dataDic = {"T": 0, "R": 0, "F": 0,"C": 0,"M": 0,"J": 0,"A": 0,"N": 0 }
    arrayLeng = len(survey)

    for i in range(0, arrayLeng):
        surveryData = survey[i]
        firstChar = surveryData[0]
        secondChar = surveryData[1]
        if choices[i] ==4 :
            continue
        if (choices[i] > 4):
            dataDic[secondChar] += (choices[i] - 4)
        if (choices[i] < 4):
            dataDic[firstChar] += (4 - choices[i])

    if dataDic["T"] > dataDic["R"]:
        answer += "T"
    elif dataDic["T"] == dataDic["R"]:
        answer += "R"
    if dataDic["T"] < dataDic["R"]:
        answer += "R"

    if dataDic["F"] > dataDic["C"]:
        answer += "F"
    elif dataDic["F"] == dataDic["C"]:
        answer += "C"
    if dataDic["F"] < dataDic["C"]:
        answer += "C"

    if dataDic["M"] > dataDic["J"]:
        answer += "M"
    elif dataDic["M"] == dataDic["J"]:
        answer += "J"
    if dataDic["M"] < dataDic["J"]:
        answer += "J"

    if dataDic["A"] > dataDic["N"]:
        answer += "A"
    elif dataDic["A"] == dataDic["N"]:
        answer += "A"
    if dataDic["A"] < dataDic["N"]:
        answer += "N"
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))