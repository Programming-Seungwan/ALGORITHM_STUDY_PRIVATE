const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [numbers, ...arr] = fs.readFileSync(filePath).toString().trim().split('\n');
const [nonHeard, nonSeen] = numbers.split(' ').map((str) => Number(str));

const firstArray = [];
const resultArray = [];

function isThereElementInArray(arr, el) {
  for (const arrEl of arr) {
    if (arrEl === el) return true;
  }
  return false;
}

for (let i = 0; i < nonHeard; i++) {
  firstArray.push(arr[i]);
}

for (let i = nonHeard; i < nonHeard + nonSeen; i++) {
  if (isThereElementInArray(firstArray, arr[i])) {
    resultArray.push(arr[i]);
  }
}

console.log(resultArray.length);
console.log(resultArray.sort().join('\n'));
