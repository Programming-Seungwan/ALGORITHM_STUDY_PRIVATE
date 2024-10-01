# from sys import stdin as s
# s = open('./input.txt', 'rt')

def turnRawTime(timeString):
    hour, minute = timeString.split(':')
    return int(hour) * 60 + int(minute)

def turnRefinedTime(timeString):
     hour = "0" + str(timeString // 60) if len(str(timeString // 60)) == 1 else str(timeString // 60)
     minute = "0" + str(timeString % 60) if len(str(timeString % 60)) == 1 else str(timeString % 60)

     return hour + ":" + minute


def solution(video_len, pos, op_start, op_end, commands):
    video_len_time = turnRawTime(video_len)
    posTime = turnRawTime(pos) # 시작점으로 활용하기
    op_start_time = turnRawTime(op_start)
    op_end_time = turnRawTime(op_end)

    commandLength = len(commands) # 명령어의 길이를 의미함
    for i in range(commandLength):
        if (posTime >= op_start_time and posTime <= op_end_time):
            posTime = op_end_time
        tmpCommandTime = 10 if commands[i] == 'next' else -10
        tmpPosTime = posTime + tmpCommandTime
        if (tmpPosTime < 0):
            posTime = 0
        elif (tmpPosTime >= video_len_time):
            posTime = video_len_time
        else:
            posTime = tmpPosTime

    if (posTime >= op_start_time and posTime <= op_end_time):
            posTime = op_end_time
    return turnRefinedTime(posTime)

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
print(solution("10:55", "00:05",	"00:15",	"06:55", ["prev", "next", "next"]))
print(solution("07:22","04:05","00:15","04:07", ["next"]))
print(solution("59:59", "59:45", "00:00", "01:00", ["next"]))
print(solution("30:00", "00:11", "05:00", "06:00", ["prev"]))
print(solution("30:35", "30:30", "01:00", "02:00", ["next"]))


