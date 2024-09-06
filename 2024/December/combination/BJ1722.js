const fs = require('fs');
const filepath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const [N, arr] = fs.readFileSync(filepath).toString().split('\n');
const n = +N;
const realArray = arr.split(' ').map((el) => Number(el));
const numberArray = [];
for (let i = 0; i < n; i++) {
  numberArray.push(i + 1);
}

// 순열을 죄다 구하고, 1이면 순열이 뭔지를 구하고 2이면 몇번째 순열인지를 출력하기

// N을 입력받아서 순열을 오름차순으로 담은 배열을 만들기
// 1이면 순서를 인덱스에서 뽑아서 출력하고, 2이면 탐색하기

// 순열의 모음을 만들어주는 함수
function getPermutations(arr) {
  const result = [];

  // 재귀적으로 순열을 생성하는 함수
  function permute(tempArr, remainingArr) {
    if (remainingArr.length === 0) {
      result.push(tempArr);
    } else {
      for (let i = 0; i < remainingArr.length; i++) {
        const newTempArr = [...tempArr, remainingArr[i]]; // 현재 요소를 추가한 배열
        const newRemainingArr = remainingArr.filter((_, index) => index !== i); // 현재 요소를 제외한 배열
        permute(newTempArr, newRemainingArr); // 재귀 호출
      }
    }
  }

  permute([], arr);
  return result;
}

// 두 배열 간의 얕은 비교를 해주는 함수
function shallowEqual(arr1, arr2) {
  return (
    arr1.length === arr2.length &&
    arr1.every((value, index) => value === arr2[index])
  );
}

const resultNumberArray = getPermutations(numberArray);

if (realArray[0] === 1) {
  console.log(resultNumberArray[realArray[1] - 1].join(' '));
} else {
  const slicedArray = realArray.slice(1);
  for (let i = 0; i < resultNumberArray.length; i++) {
    if (shallowEqual(resultNumberArray[i], slicedArray)) {
      console.log(i + 1);
    }
  }
}
