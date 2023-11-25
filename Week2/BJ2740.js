// 백준 2740 행렬 곱셈 문제
// https://www.acmicpc.net/problem/2740
const fs = require('fs');
let inputArray = fs.readFileSync('./input.txt').toString().trim().split('\r\n')[0].split('\n');
// 실제로 사용할 InputArray
let realInputArray = [];

for (let i = 0; i < inputArray.length; i++) {
  realInputArray.push(inputArray[i].split(' ').map((v) => parseInt(v)));
}

// 우선 특정 배열에 넣어줄 필요가 있다.
const firstArray = [];
const secondArray = [];
let realInputArrayIndex = 0;

const firstArrayRowLength = realInputArray[0][0];
const firstArrayColumnLength = realInputArray[0][1];

for (let i = 1; i <= firstArrayRowLength; i++) {
  firstArray.push(realInputArray[i]);
}

const secondArrayRowLength = realInputArray[firstArrayRowLength + 1][0];
const secondArrayColumnLength = realInputArray[firstArrayRowLength + 1][1];

for (let i = firstArrayRowLength + 2; i < realInputArray.length; i++) {
  secondArray.push(realInputArray[i]);
}

function multiplyMatrix(matrixA, matrixB) {
  let result = [];

  for (let i = 0; i < matrixA.length; i++) {
    result[i] = [];
    for (let j = 0; j < matrixB[0].length; j++) {
      result[i][j] = 0;
      for (let k = 0; k < matrixA[0].length; k++) {
        result[i][j] += matrixA[i][k] * matrixB[k][j];
      }
    }
  }

  return result;
}

const result = multiplyMatrix(firstArray, secondArray);

for (let i = 0; i < result.length; i++) {
  console.log(result[i].join(' '));
}
