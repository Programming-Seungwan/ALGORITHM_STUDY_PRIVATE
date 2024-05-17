def solution(s):
    answer = len(s)

    # step은 압축 단위를 의미함
    for step in range(1, len(s) // 2 + 1):
        compressed = '' # 우선 빈 문자열로 만들어주기

        prev = s[0 : step] # 반복될 문자열을 의미함
        count = 1 # 몇 번 반복될지를 의미함

        # j는 1부터 시작하며 시작점을 의미할 수 있음
        for j in range(step, len(s), step): # step은 고정적인 것이고 j는 그 내부를 순환하면서 변하는 유동적인 값이다. step부터 할 수 있는 이유는 첫 한 턴의 문자열은 비교하는 것이 의미가 없기 떄문이다
            if prev == s[j: j + step]:
                count += 1
            # 더 이상 나아간 새로운 step 길이의 문자열이 prev 문자열(길이는 step)과 같지 않은 경우
            else:
                compressed += str(count) + prev if count >= 2 else prev # 람다식을 이용해 2 이상이면 숫자prev를, 1이면 그냥 prev만 붙여주는 것을 의미함
                prev = s[j: j + step] #일치하지 않은 것으로 prev를 맞춰줌
                count = 1 # count도 다시 1로 만들어줌

        compressed += str(count) + prev if count >= 2 else prev # 마지막 for문이 끝났는데 처리되지 않은 count와 prev를 문자열에 반영해줌
        answer = min(answer, len(compressed))

    return answer