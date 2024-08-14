const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [numbers, ...arr] = fs.readFileSync(filePath).toString().trim().split('\n');
const [nonHeard, nonSeen] = numbers.split(' ').map((str) => Number(str));

const firstObject = {};
const resultArray = [];

for (let i = 0; i < nonHeard; i++) {
  firstObject[arr[i]] = 1;
}

for (let i = nonHeard; i < nonHeard + nonSeen; i++) {
  if (firstObject[arr[i]]) {
    resultArray.push(arr[i]);
  }
}

console.log(resultArray.length);
console.log(resultArray.sort().join('\n'));
