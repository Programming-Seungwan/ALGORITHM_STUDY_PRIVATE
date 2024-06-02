def solution(m, musicinfos):
    answer = ""
    answerList = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", 'b')
    for musicInfo in musicinfos:
        splitInfo = musicInfo.split(',')
        # print(splitInfo)
        splitInfo[3] = splitInfo[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", 'b')
        startInfo = splitInfo[0].split(':')
        startTime = int(startInfo[0]) * 60 + int(startInfo[1])
        endInfo = splitInfo[1].split(':')
        endTime = int(endInfo[0]) * 60 + int(endInfo[1])
        spendTime = endTime - startTime # 재생된 시각에 해당
        songLength = len(splitInfo[3])
        times = spendTime // songLength
        realPlayedSong = splitInfo[3] * times + splitInfo[3][: spendTime % songLength]

        # print(realPlayedSong)
        if (m in realPlayedSong):
            answerList.append([spendTime, splitInfo[2]])
    # print(answerList)

    if not answerList:
        return "(None)"

    maxLength = answerList[0][0]

    if len(answerList) != 0:
         answer = answerList[0][1]
         for i in range(0, len(answerList)):
            if (answerList[i][0] > maxLength):
                answer = answerList[i][1]
                maxLength = answerList[i][0]


    return answer

