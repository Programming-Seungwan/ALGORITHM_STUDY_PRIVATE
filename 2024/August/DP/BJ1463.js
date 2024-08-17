const fs = require('fs')
const filePath = process.platform === 'linux' ? "/dev/stdin" : './input.txt';
const number = Number(fs.readFileSync(filePath).toString().trim())

const memoArray = new Array(number + 1).fill(Infinity);
memoArray[1] = 0;
memoArray[2] = 1;
function getResult(incomeNumber) {
  const tmpArray = []
  if (incomeNumber % 3 === 0) {
    tmpArray.push(incomeNumber / 3);
  }
  if (incomeNumber % 2 === 0) {
    tmpArray.push(incomeNumber / 2);
  }
  tmpArray.push(incomeNumber - 1);

  return tmpArray
}

for (let i = 2; i <= number; i++) {
  const result = getResult(i);
  const minResult = Math.min(...result.map((element) => {
    return memoArray[element]
  }))
  memoArray[i] = memoArray[i] < minResult + 1 ? memoArray[i] : minResult + 1;

}

console.log(memoArray[number])

