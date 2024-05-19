def isAllcleared(dataList):
  for data in dataList:
    if data != 0:
      return False
  return True


# 수거할 것과 배달할 것이 남아있는 마지막 집의 index를 가져오는 함수
def getPossibleHouseIndex(deliveryList, pickUpsList):
   homeLength = len(deliveryList)
   for i in range(homeLength - 1, -1, -1):
      if deliveryList[i] != 0 or pickUpsList[i] != 0:
         return i
      if (deliveryList[i] == 0 and pickUpsList[i] == 0) and (deliveryList[i -1] != 0 and pickUpsList[i - 1] != 0):
         return i - 1

def solution(cap, n, deliveries, pickups):
    # 모든 배달, 수거 관련된 데이터가 0일 때까지 진행
    distance = 0

    while(not isAllcleared(deliveries) or not isAllcleared(pickups)):
       truckDeliverCap = cap
       truckPickupCap = cap
       tmpIndex = getPossibleHouseIndex(deliveries, pickups)

       for i in range(tmpIndex, -1, -1):
          # 지정된 것에서 거꾸로 가면서 1이상이고, 아직 truckCap이 남았으면 그만큼 빼주자
          if (deliveries[i] >= 1 and truckDeliverCap > 0):
             delSubValue = min(truckDeliverCap, deliveries[i])
             deliveries[i] -= delSubValue
             truckDeliverCap = truckDeliverCap - delSubValue

          if (pickups[i] >= 1 and truckPickupCap > 0):
             pickSubValue = min(truckPickupCap, pickups[i])
             pickups[i] -= pickSubValue
             truckPickupCap = truckPickupCap - pickSubValue


       distance += (2 * (tmpIndex + 1))

    return distance
