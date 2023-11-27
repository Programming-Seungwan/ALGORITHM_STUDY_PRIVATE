// 백준 1654번 랜선 자르기 문제
// https://www.acmicpc.net/problem/1654

const fs = require('fs');
const { start } = require('repl');

let [nAndK, ...arr] = fs.readFileSync('./input.txt').toString().trim().split('\n');

const [n, k] = nAndK.split(' ').map((el) => parseInt(el));

arr = arr.map((el) => parseInt(el));
// n, k, arr 처리 완료

arr.sort((a, b) => a - b);

// 개수를 구하는 함수
function getWireNum(array, wireLength) {
  let result = 0;
  for (const a of array) result += Math.floor(a / wireLength);
  return result;
}

// targetAmount 만들고자 하는 랜선의 개수이다. 이보다 크기만 하면 됨
// targetAmount보다 크면 (mid, 기본 end + mid / 2), 작으면 ()
function solution(startNum, endNum, targetAmount) {
  if (startNum === endNum || startNum + 1 === endNum) return startNum;

  const midNum = Math.floor((startNum + endNum) / 2);

  if (getWireNum(arr, midNum) >= targetAmount) {
    return solution(midNum, endNum, targetAmount);
  } else {
    return solution(startNum, midNum, targetAmount);
  }
}

console.log(solution(1, arr[arr.length - 1], k));
