const fs = require('fs');
const filepath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const [n, ...arr] = fs.readFileSync(filepath).toString().trim().split('\n');
const realArr = arr.map((el) => +el);

realArr.sort((a, b) => a - b);
const realArrLength = realArr.length;

let resultSum = 0; // 비교 횟수를 말할 변수임
for (let i = 0; i < realArr.length; i++) {
  if (i === 0 || i === 1) {
    resultSum += realArr[i] * (realArrLength - 1);
  } else {
    resultSum += realArr[i] * (realArrLength - i);
  }
}

console.log(resultSum);
