def check(s): # 올바른 문자열인지를 확인하는 함수
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0: # )가 들어왔는데 기존에 아무것도 없으면 올바른 문자열이 아님
                return False
            stack.pop()
    return True

def divide(s):
    left, right = 0,0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right: # 더 이상 쪼개질 수 없는 균형 잡힌 문자열로 만드는 것이니까 매번 비교해서 숫자가 같으면 바로 거기까지만 하고 return
            return s[:i+1], s[i+1:]

def solution(p):
    if not p:
        return ''

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for s in u[1:len(u)-1]:
            if s == '(': # 뒤집기
                answer += ')'
            else:
                answer += '('
        return answer