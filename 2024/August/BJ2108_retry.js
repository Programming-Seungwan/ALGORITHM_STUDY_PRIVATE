const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let [n, ...arr] = fs.readFileSync(filePath).toString().trim().split('\n').map((str) => Number(str));

if (n === 1) {
  console.log(arr[0])
  console.log(arr[0])
  console.log(arr[0])
  console.log(0)
} else {
  let average = 0; // 산술 평균을 의미
  let middleNum = 0; // 중앙값을 의미
  let commonNum = 0; // 최빈값을 의미
  let range = 0; // 범위를 의미

  const sum = arr.reduce((acc, val) => acc + val, 0)
  average = Math.round((sum / n)) === 0 ? Math.abs(Math.round((sum / n))) : Math.round((sum / n))
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
      return a[0] - b[0]
    }
  })

  commonNum = memoArray[0][1] === memoArray[1][1] ? memoArray[1][0] : memoArray[0][0]
  range = Math.abs(arr[n - 1] - arr[0])

  console.log(average)
  console.log(middleNum)
  console.log(commonNum)
  console.log(range)
}