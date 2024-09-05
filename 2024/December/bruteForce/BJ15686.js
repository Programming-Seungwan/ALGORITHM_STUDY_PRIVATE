const fs = require('fs');
const filepath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const [num, ...arr] = fs.readFileSync(filepath).toString().trim().split('\n');
const [N, M] = num.split(' ').map((element) => Number(element));
const realArr = arr.map((element) =>
  element.split(' ').map((el) => Number(el))
);

function getDistance(housePoint, chickenPoint) {
  return (
    Math.abs(housePoint[0] - chickenPoint[0]) +
    Math.abs(housePoint[1] - chickenPoint[1])
  );
}

function getMinChickenDistance(houseArr, newChickenArr) {
  let minDistance = 0;
  for (const housePtr of houseArr) {
    const distanceArr = [];
    for (const newChickenPtr of newChickenArr) {
      distanceArr.push(getDistance(housePtr, newChickenPtr));
    }
    minDistance += Math.min(...distanceArr);
  }

  return minDistance;
}

function getCombinations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1); // 고정된 값 이후의 요소들
    const combinations = getCombinations(rest, selectNumber - 1); // 재귀적으로 조합 생성
    const attached = combinations.map((combination) => [fixed, ...combination]); // 고정된 값에 조합 붙이기
    results.push(...attached);
  });

  return results;
}

const houseArr = [];
const chickenArr = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (realArr[i][j] === 1) {
      houseArr.push([i + 1, j + 1]);
    } else if (realArr[i][j] === 2) {
      chickenArr.push([i + 1, j + 1]);
    }
  }
}

const mChickenArray = getCombinations(chickenArr, M);
const resultArray = [];
for (const newChicken of mChickenArray) {
  resultArray.push(getMinChickenDistance(houseArr, newChicken));
}

console.log(Math.min(...resultArray));
