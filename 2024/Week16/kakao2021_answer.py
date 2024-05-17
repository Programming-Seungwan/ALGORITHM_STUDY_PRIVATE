from itertools import combinations

def solution(orders, course):
    answer = []

    for course_item in course:
        comb_count = {} # 실제로 존재하는 콤비네이션들만 늘려가면서 카운트임
        max_order = []
        for order in orders:
            order_comb = combinations(list(order), course_item) # 특정 사람의 주문에서 조합을 뽑아낸다

            for comb in order_comb:
                order_comb_string = "".join(sorted(comb))

                if comb_count.get(order_comb_string): # 딕셔너리의 개념을 활용함. 특정 요소가 있으면 1 늘려주고, 없으면 1로 셋팅해주고
                    comb_count[order_comb_string] += 1

                else:
                    comb_count[order_comb_string] = 1

        max_order = [k for k,v in comb_count.items() if ((v == max(comb_count.values())) and v >= 2) ] # 현재 메뉴가짓수에서 가장 크다면 k로 max_order를 지정함

        answer.extend(max_order)

    answer = sorted(answer)
    return answer