// 토마토의 개수를 센다. 하루가 지날때마다 점검을 한다.
// 점검은 어떻게 하는가? 전체 배열을 돌면서 1의 개수를 센다.
// 하루가 지나고 토마토 판을 갱신하는 것은 어떻게 하는가? 기존의 것을 복사해놓는다. 이전 토마토와 다음 토마토 판을 구분해서 자료구조로 저장한다
// while문을 언제 끝낼 것인가? 다 익었을 경우, 더이상 익지 못하는 경우(기존의 것과 동일한 경우)
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const [firstLine, ...arr] = fs.readFileSync(filePath).toString().split('\n');
const [M, N] = firstLine.split(' ').map((el) => parseInt(el));
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

let refinedArr = arr.map((element) =>
  element.split(' ').map((el) => parseInt(el))
);

const totalTomatoCount = refinedArr
  .flat()
  .filter((element) => element === 0 || element === 1).length;

let ripenTomato = refinedArr
  .flat()
  .reduce((prev, element) => prev + (element === 1 ? 1 : 0), 0);

if (ripenTomato === totalTomatoCount) {
  console.log(0);
  process.exit(0);
}

let dayCount = 0;

// 토마토가 다 익었는가를 판단하는 함수
function isTwoArrayCompletelyEqual(arr1, arr2) {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr1[i][j] !== arr2[i][j]) return false;
    }
  }

  return true;
}

// 익은 토마토의 개수를 판단하는 함수
function getRipenTomatoCount(arr) {
  let resultCount = 0;
  for (const el of arr) {
    for (const element of el) {
      if (element === 0 || element === 1) {
        resultCount += 1;
      }
    }
  }

  return resultCount;
}

// 해당 거기 안에서 다음 날의 rotten 배열을 만들어주고, 상태가 같지 않으면 daycount를 늘려주고 같으면 끝내버리기
// 해당 배열을 어떻게 그래프로 나타낼 것인가?
while (true) {
  const visited = Array.from({ length: N }, () => Array(M).fill(false));
  const newRefinedArr = JSON.parse(JSON.stringify(refinedArr));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (refinedArr[i][j] === 1) {
        for (let k = 0; k < 4; k++) {
          const nextX = i + dx[k];
          const nextY = j + dy[k];
          if (
            nextX >= 0 &&
            nextX < N &&
            nextY >= 0 &&
            nextY < M &&
            refinedArr[nextX][nextY] === 0 &&
            !visited[nextX][nextY]
          ) {
            newRefinedArr[nextX][nextY] = 1;
            visited[nextX][nextY] = true;
          }
        }
      }
    }
  }

  if (
    getRipenTomatoCount(newRefinedArr) === totalTomatoCount &&
    isTwoArrayCompletelyEqual(refinedArr, newRefinedArr)
  ) {
    break;
  } else {
    refinedArr = newRefinedArr;
    dayCount += 1;
  }
}

console.log(dayCount);
