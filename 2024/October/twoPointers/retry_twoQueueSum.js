// 1이 먼저인지 2가 먼저인지도 포인트임 -> 왼쪽 오른쪽은 크게 상관 없음. 왜냐? 어차피 원형 큐이기 때문임
// 사용자가 바깥에 숫자 그룹을 가지고 있는가?
function solution(queue1, queue2) {
  // 두 큐를 합친다 -> totalArray
  const totalArray = [...queue1, ...queue2];
  // left와 right를 각각 큐1의 처음과 끝으로 설정한다.
  let leftPointer = 0;
  let rightPointer = queue1.length - 1;
  const targetSum = totalArray.reduce((prev, curr) => prev + curr, 0) / 2;
  let sum = totalArray
    .slice(leftPointer, rightPointer + 1)
    .reduce((prev, curr) => prev + curr, 0);

  let minCount = Infinity; // 최소 숫자에 대응하는 개념이다
  let count = 0; // 이건 활용할 카운트 변수

  while (rightPointer < totalArray.length - 1) {
    // 사실 모든 경우를 다 뒤져보는데 최대한 효율적으로 하고자 하는 알고리즘임

    while (sum >= targetSum) {
      // 포인터 이동 전에 먼저 빼야함
      sum -= totalArray[leftPointer];
      leftPointer += 1;
      count += 1;
      if (sum === targetSum) {
        minCount = Math.min(minCount, count);
        break;
      }
    }

    rightPointer += 1;
    count += 1; // 카운트를 늘려주기
    sum += totalArray[rightPointer]; // 새로 나온 거를 더해준다.
  }

  minCount = minCount === Infinity ? -1 : minCount;

  return minCount;

  // while문을 돌리는데, 합이 목표 수치를 넘어서는 가를 체크한다.
  // 넘어서면 left를 늘리면서 감소시켜 언제까지 가능한가를 본다.
  // minCount를 반환한다!
}

console.log(solution([3, 2, 7, 2], [4, 6, 5, 1]));
console.log(solution([1, 2, 1, 2], [1, 10, 1, 2]));
console.log(solution([1, 1], [1, 5]));
