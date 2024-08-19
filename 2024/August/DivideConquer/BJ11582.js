const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const rawArray = fs.readFileSync(filePath).toString().trim().split('\n');
const N = BigInt(rawArray[0]);
const numberArray = rawArray[1].split(' ').map(Number);
const K = BigInt(rawArray[2]);

const arrayElementCount = Number(N / K);
let tmpArray = [];
for (let i = 0; i < N; i += arrayElementCount) {
  tmpArray.push(numberArray.slice(i, i + arrayElementCount));
}

for (let i = 0; i < K; i++) {
  tmpArray[i].sort((a, b) => a - b);
}
const resultArray = [];
tmpArray.map((element) => {
  for (let i = 0; i < arrayElementCount; i++) {
    resultArray.push(element[i]);
  }
});

console.log(resultArray.join(' '));
