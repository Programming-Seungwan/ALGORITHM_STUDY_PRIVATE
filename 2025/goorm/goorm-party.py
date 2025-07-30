# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))  # 1-based indexing

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        # 작은 번호가 루트가 되도록
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py

# 노드 별 시그널 결과를 만들어내는 함수임.
# 우선 클래스 인스턴스를 만들고, 이걸 기반으로 edge마다 union을 해서 내부 parent를 프로세싱함.
# 그 다음 각 노드에 맞는 시그널을 출력해냄
def find_min_reachable_nodes(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)

    result = []
    for i in range(1, n + 1):
        result.append(uf.find(i))
    return result

user_input = input().split(' ')
N = int(user_input[0])
M = int(user_input[1])

islandList = list(map(int, input().split(' ')))
bridgeInfoList = []
for i in range(M):
	bridgeInfoList.append(list(map(int, input().split(' '))))

uf_results = find_min_reachable_nodes(N, bridgeInfoList)

totalResult = 0
for i in range(len(islandList)):
	if uf_results[i] == 1:
		totalResult += islandList[i]

print(totalResult)
