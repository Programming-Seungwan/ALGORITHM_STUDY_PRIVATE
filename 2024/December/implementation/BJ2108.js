const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const [n, ...arr] = fs.readFileSync(filePath).toString().split('\n');

const realN = parseInt(n);
const realArr = arr
  .map((element) => element.replace('\r', ''))
  .map((el) => parseInt(el));

// 산술평균
// 중앙값
// 최빈값 -> 여러 개 있으면 두번째로 작은것을 추출
// 범위
// 정렬 하고, 객체에 때려넣어서 저장한 다음 순회하면서 GET
const memoDictionary = {};
realArr.sort((a, b) => a - b);

for (const element of realArr) {
  if (memoDictionary[element]) {
    memoDictionary[element] += 1;
  } else {
    memoDictionary[element] = 1;
  }
}

// 최빈값을 구하는
function getFrequentNumberInDictionary(dic) {
  let resultArray = [];
  let resultValue = 0;

  for (const k in dic) {
    if (dic[k] > resultValue) {
      resultValue = dic[k];
      resultArray = [];
      resultArray.push(parseInt(k));
    } else if (dic[k] === resultValue) {
      resultArray.push(parseInt(k));
    }
  }

  resultArray.sort((a, b) => a - b);
  if (resultArray.length === 1) {
    return resultArray[0];
  } else {
    return resultArray[1];
  }
}

console.log(
  Math.round(realArr.reduce((prev, element) => prev + element, 0) / realN) ===
    -0
    ? 0
    : Math.round(realArr.reduce((prev, element) => prev + element, 0) / realN)
);
console.log(realArr[Math.floor(realN / 2)]);
console.log(getFrequentNumberInDictionary(memoDictionary));
console.log(realArr[realArr.length - 1] - realArr[0]);
