def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4: # 1의 자리수가 5일 때에는 10의 자리수의 크기 여부를 본다
                storey += 10
            answer += remainder
        storey //= 10

    return answer