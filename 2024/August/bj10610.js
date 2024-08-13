const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const num = fs.readFileSync(filePath).toString().trim()
const numArray = num.split('').map((element) => BigInt(element))

const hasZero = numArray.some((number) => number === 0n)

if (!hasZero) {
  console.log(-1)
} else {
  const totalSum = numArray.reduce((acc, income) => acc + income, 0n)
  if (totalSum % 3n !== 0n) {
    console.log(-1)
  } else {
    console.log(numArray.sort((a, b) => Number(b) - Number(a)).join(''))
  }
}