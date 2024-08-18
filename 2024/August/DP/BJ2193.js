const fs = require('fs')
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const number = Number(fs.readFileSync(filePath).toString().trim())

const memoObject = {}

function isPinaryNumber(prevNumber, binaryNumber) {
  if (binaryNumber === 0) {
    return true
  } else if (binaryNumber === 1) {
    const prevNumberString = String(prevNumber);
    return prevNumberString[prevNumberString.length - 1] === '1' ? false : true;
  }
}

memoObject[1] = [1];
for (let i = 2; i <= number; i++) {
  memoObject[i] = [];
  for (const prevMemoNumber of memoObject[i - 1]) {
    if (isPinaryNumber(prevMemoNumber, 0)) {
      memoObject[i].push(String(prevMemoNumber).concat('0'))
    }

    if (isPinaryNumber(prevMemoNumber, 1)) {
      memoObject[i].push(String(prevMemoNumber).concat('1'))
    }
  }
}

console.log(memoObject[number].length)