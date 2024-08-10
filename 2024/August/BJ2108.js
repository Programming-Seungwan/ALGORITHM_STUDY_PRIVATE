const fs = require('fs');
let [n, ...arr] = fs.readFileSync('./input.txt').toString().trim().split('\n').map((str) => Number(str));

let average = 0; // 산술 평균을 의미
let middleNum = 0; // 중앙값을 의미
let commonNum = 0; // 최빈값을 의미
let range = 0; // 범위를 의미

const sum = arr.reduce((acc, val) => acc + val, 0)
average = Math.round((sum / n) + 1) - 1;
arr.sort()
middleNum = arr[Math.floor(n/2)]
const memoObject = {}
for (const num of arr) {
  if (!memoObject[num]) {
    memoObject[num] = 1
  } else {
    memoObject[num] += 1
  }
}

const memoArray = []
for (const num in memoObject) {
  memoArray.push([Number(num), memoObject[num]])
}

memoArray.sort((a, b) => {
  if (b[1] !== a[1]) {
    return b[1] - a[1]
  } else {
    b[0] - a[0]
  }
})

commonNum = memoArray[0][1] === memoArray[1][1] ? memoArray[0][0] : memoArray[1][0]

range = arr[n - 1] - arr[0]

console.log(average)
console.log(middleNum)
console.log(commonNum)
console.log(range)