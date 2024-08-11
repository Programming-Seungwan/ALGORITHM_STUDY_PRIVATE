const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const num = Number(fs.readFileSync(filePath).toString().trim())
const numArray = String(num).split('').map((element) => Number(element))
const hasZero = numArray.some((number) => number === 0)

if (!hasZero) {
  console.log(-1)
} else {
  const totalSum = numArray.reduce((acc, income) => acc + income, 0)
  if (totalSum % 3 !== 0) {
    console.log(-1)
  } else {
    console.log(Number(numArray.sort((a, b) => b - a).join('')))
  }
}