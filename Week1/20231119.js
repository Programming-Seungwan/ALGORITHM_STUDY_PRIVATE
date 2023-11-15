// 백준 설탕 배달 문제
// https://www.acmicpc.net/problem/2839

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const n = Number(input);

function solution(number) {
  // 기록을 진행해줄 배열을 만든다
  const memoArray = new Array(number + 1);
  memoArray[0] = -1;
  memoArray[1] = -1;
  memoArray[2] = -1;
  memoArray[3] = 1;
  memoArray[4] = -1;
  memoArray[5] = 1;

  // Bottom - up 방식으로 해당 number까지 쌓아 올라가는 방식을 택한다
  for (let i = 6; i < number + 1; i++) {
    // 3과 5를 뺀 케이스가 둘다 -1인 경우라면 역시 -1로 기록
    if (memoArray[i - 3] === -1 && memoArray[i - 5] === -1) {
      memoArray[i] = -1;
      continue;
    }
    if (memoArray[i - 3] === -1 && memoArray[i - 5] !== -1) {
      memoArray[i] = memoArray[i - 5] + 1;
      continue;
    }
    if (memoArray[i - 3] !== -1 && memoArray[i - 5] === -1) {
      memoArray[i] = memoArray[i - 3] + 1;
      continue;
    }

    // 3과 5를 뺀 기록 결과 중 작은 것에서 1을 더한 결과를 기록
    memoArray[i] = memoArray[i - 3] < memoArray[i - 5] ? memoArray[i - 3] + 1 : memoArray[i - 5] + 1;
  }

  return memoArray[number];
}

console.log(solution(n));
