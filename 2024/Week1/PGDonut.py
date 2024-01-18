def solution(edges):
  mapDictionary = {}
  # 각 vertex를 정리한다
  for edge in edges:
    if edge[0] not in mapDictionary:
      mapDictionary[edge[0]] = {'give' : [], 'receive': []}
      mapDictionary[edge[0]]['give'].append(edge[1])
    else:
      mapDictionary[edge[0]]['give'].append(edge[1])

    if edge[1] not in mapDictionary:
      mapDictionary[edge[1]] = {'give' : [], 'receive': []}
      mapDictionary[edge[1]]['receive'].append(edge[0])
    else:
      mapDictionary[edge[1]]['receive'].append(edge[0])

  # 생성한 정점을 찾는 로직
  makeVertex = 0
  for key in mapDictionary:
    if len(mapDictionary[key]['give']) >= 2 and len(mapDictionary[key]['receive']) == 0:
      makeVertex = key
      break

  # 생성한 정점으로부터 연결되는 간선의 개수, 즉 총 그래프의 개수를 의미
  totalGraphNum = len(mapDictionary[makeVertex]['give'])

  # makeVertex와 연결된 그래프와의 간선을 끊어주는 로직
  for _ in range(totalGraphNum):
    tmpConnectedGraphVertex = mapDictionary[makeVertex]['give'].pop()
    mapDictionary[tmpConnectedGraphVertex]['receive'].remove(makeVertex)

  # 막대 그래프의 개수를 찾는 로직
  # 근데 makeVertex도 모든 연결된 간선을 다 끊어주었기에 카운트하면 안됨
  stickNum = 0
  for key in mapDictionary:
    if key == makeVertex:
      continue
    if len(mapDictionary[key]['give']) == 0:
      stickNum += 1

  # 8자 그래프의 개수를 찾는 로직
  eightNum = 0
  for key in mapDictionary:

    if len(mapDictionary[key]['give']) == 2 and len(mapDictionary[key]['receive']) == 2:
      eightNum += 1

  donutNum = totalGraphNum - stickNum - eightNum

  return [makeVertex, donutNum, stickNum, eightNum]

solution([[2, 3], [4, 3], [1, 1], [2, 1]])
