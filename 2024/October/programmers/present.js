// 두 사람 간에 우위가 있으면 많이 준 사람이 다음 달에 하나 받고, 이력이 없거나 같다면 얼마나 많이 베풀었는지의 선물 지수로 비교함
// 자료 구조로 깔끔하게 정리를 해놓기. 객체 자료형을 사용. 각 사람들을 돌면서 다른 사람들과 어떤 관계에 있어 선물을 받는지 측정
// 사람마다 다음 달에 받을 선물의 카운트를 정해놓기

function solution(friends, gifts) {
  const giftGivingHistoryObject = {};
  const giftReceivingHistoryObject = {};
  const nextMonthResult = {};
  for (const person of friends) {
    giftGivingHistoryObject[person] = {};
    giftReceivingHistoryObject[person] = {};
    nextMonthResult[person] = 0;
  }

  for (const history of gifts) {
    const [giver, receiver] = history.split(' ');
    if (!giftGivingHistoryObject[giver][receiver]) {
      giftGivingHistoryObject[giver][receiver] = 1;
    } else {
      giftGivingHistoryObject[giver][receiver] += 1;
    }

    if (!giftReceivingHistoryObject[receiver][giver]) {
      giftReceivingHistoryObject[receiver][giver] = 1;
    } else {
      giftReceivingHistoryObject[receiver][giver] += 1;
    }
  }

  // console.log(giftGivingHistoryObject)
  // console.log(giftReceivingHistoryObject)

  for (const standardPerson of friends) {
    for (const comparingPerson of friends) {
      if (standardPerson !== comparingPerson) {
        if (
          giftGivingHistoryObject[standardPerson][comparingPerson] >
          giftGivingHistoryObject[comparingPerson][standardPerson]
        ) {
          nextMonthResult[standardPerson] += 1;
        } else if (
          giftGivingHistoryObject[standardPerson][comparingPerson] <
          giftGivingHistoryObject[comparingPerson][standardPerson]
        ) {
          nextMonthResult[comparingPerson] += 1;
        } else {
          let standardPersonIndex = 0;
          let comparingPersonIndex = 0;
          for (const tmpValue in giftGivingHistoryObject[standardPerson]) {
            standardPersonIndex +=
              giftGivingHistoryObject[standardPerson][tmpValue];
          }

          for (const tmpValue in [standardPerson]) {
            standardPersonIndex -=
              giftReceivingHistoryObject[standardPerson][tmpValue];
          }

          for (const tmpValue in giftGivingHistoryObject[comparingPerson]) {
            standardPersonIndex +=
              giftGivingHistoryObject[comparingPerson][tmpValue];
          }

          for (const tmpValue in [comparingPerson]) {
            standardPersonIndex -=
              giftReceivingHistoryObject[comparingPerson][tmpValue];
          }

          if (standardPersonIndex > comparingPersonIndex) {
            nextMonthResult[standardPerson] += 1;
          } else if (standardPersonIndex < comparingPersonIndex) {
            nextMonthResult[comparingPerson] += 1;
          }
        }
      }
    }
  }

  console.log(nextMonthResult);
}
