import sys

ans = 0
ins = sys.stdin.readline() # 괄호 입력
stack = [] # 스택 배열

top = -1 # 스택 top 의 인덱스
for idx, i in enumerate(ins):
    if i == '(':
        stack.append(idx)
        top = idx

    elif i == ')':
        if top == idx - 1:
            stack.pop()
            if stack:
                top = stack[-1]
            else:
                top = -1
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
            if stack:
                top = stack[-1]
            else:
                top = -1

print(ans)