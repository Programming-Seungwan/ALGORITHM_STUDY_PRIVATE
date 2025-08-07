const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const arr = fs.readFileSync(filePath).toString().trim().split('\n');
const havingCardArray = arr[1]
  .split(' ')
  .map((el) => +el)
  .sort((a, b) => a - b);

const givenCardArray = arr[3].split(' ').map((el) => +el);

const binarySearch = (arr, targetItem) => {
  let start = 0;
  let end = arr.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);

    if (arr[mid] === targetItem) {
      return 1;
    } else if (arr[mid] < targetItem) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return 0;
};

const resultArray = [];

binarySearch(havingCardArray, givenCardArray[0]);

for (const givenCardNumber of givenCardArray) {
  resultArray.push(binarySearch(havingCardArray, givenCardNumber));
}

console.log(resultArray.join(' '));
