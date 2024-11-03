// 숫자를 원소로 하는 두 배열을 받아 각각 이진수로 바꾸고 이를 하나의 지도로 만들어서 반환하기
// 1. 이진수를 만드는 함수 작성

// 2. 두 지도를 합치는 로직

// 3. 해당 로직을 배열에 담아서 반환

function fromDecimalToBinary(originalNumber) {
  let remainNumber = originalNumber; // 0으로 만들 숫자
  let result = '';
  while (remainNumber > 0) {
    if (remainNumber % 2 === 1) {
      result += '1';
    } else {
      result += '0';
    }
    remainNumber = Math.floor(remainNumber / 2);
  }

  return result.split('').reverse().join('');
}

function solution(n, arr1, arr2) {
  let arr1Map = [];
  let arr2Map = [];
  const arrLength = arr1.length;
  const tmpArray = [];

  for (const el of arr1) {
    arr1Map.push(fromDecimalToBinary(el));
  }

  for (const el of arr2) {
    arr2Map.push(fromDecimalToBinary(el));
  }

  for (let i = 0; i < arrLength; i++) {
    const first = arr1Map[i];
    const second = arr2Map[i];
    let tmpResultString = '';
    for (let j = 0; j < n; j++) {
      if (first[j] === '0' && second[j] === '0') {
        tmpResultString += '0';
      } else {
        tmpResultString += '1';
      }
    }
    tmpArray.push(tmpResultString);
  }

  return tmpArray;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
