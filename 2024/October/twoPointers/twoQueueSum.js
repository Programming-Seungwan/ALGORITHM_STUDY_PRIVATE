// 빼서 넣어주는 것이 작업 1회임
// 조합을 만들어서 그룹을 나누어주면 됨.

// 1. 목표 숫자를 정한다.
// 2. 조합 구성을 구한다...?
// 원형 큐로 생각할 수 있는 이유? 슬라이딩을 하는 것 자체가 배열 a에서 pop한 것을 b에 insert 하는 현상이 일종의 sliding으로 생각할 수 있기 떄문이다.
// 포인터를 동시에 움직이면 그건 또 안됨. 그렇다면 배열이 거꾸로 맞물려도 되는가?

function solution(queue1, queue2) {
  const circleQueueArray = [...queue1, ...queue2]; // 원형 큐로 만들어줌
  const totalSum = circleQueueArray.reduce((prev, curr) => prev + curr, 0);

  if (totalSum % 2 !== 0) return -1; // 전체 합이 홀수인 경우 불가능함
  const targetSum = totalSum / 2;

  const sliderLength = queue1.length;
  let startPoint = 0;
  let endPoint = startPoint + sliderLength - 1;
  let workCount = 0; // 작업의 횟수에 해당함

  while (true) {
    let tmpSum = circleQueueArray.splice(startPoint, endPoint + 1);
    if (tmpSum === targetSum) {
      return (workCount += 1);
    }

    startPoint += 1;
    workCount += 1;
    tmpSum = circleQueueArray.splice(startPoint, endPoint + 1);
    if (tmpSum === targetSum) {
      return workCount;
    }
    endPoint += 1;
    if (endPoint === circleQueueArray.length) {
      break;
    }
    workCount += 1;
    tmpSum = circleQueueArray.splice(startPoint, endPoint + 1);
    if (tmpSum === targetSum) {
      return workCount;
    }
  }

  return -1;
}
