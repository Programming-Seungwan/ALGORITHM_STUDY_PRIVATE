// 백준 11279 최대 힙 문제
// https://www.acmicpc.net/problem/11279
const fs = require('fs');
const [n, ...dtarray] = fs
  .readFileSync('./input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((v) => Number(v));

// 배열의 두 요소를 swap 해주는 기능의 함수
function swapArrayElement(arr, indexOne, indexTwo) {
  const tmp = arr[indexOne];
  arr[indexOne] = arr[indexTwo];
  arr[indexTwo] = tmp;
}

const dataArray = [];

// 최대 히프에 새로운 숫자를 삽입하는 함수
function pushNewElementToArray(myarr, newNumber) {
  if (myarr.length === 0) {
    myarr.push(newNumber);
    return;
  }

  myarr.push(newNumber);
  let newNumberIndex = myarr.length - 1;

  while (true) {
    let parentIndex = newNumberIndex / 2;
    if (newNumberIndex % 2 === 0) {
      parentIndex = newNumberIndex / 2 - 1;
    } else {
      parentIndex = (newNumberIndex - 1) / 2;
    }

    if (myarr[newNumberIndex] > myarr[parentIndex]) {
      swapArrayElement(myarr, newNumberIndex, parentIndex);
      newNumberIndex = parentIndex;
    } else break;
  }
}

// 최대 히프를 trickle down하는 함수가 추가로 필요하다

function trickleDown(myarr, index) {
  while (true) {
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    if (leftChildIndex === undefined && rightChildIndex === undefined) return;
    if (leftChildIndex !== undefined && rightChildIndex === undefined) {
      if (myarr[index] < myarr[leftChildIndex]) {
        swapArrayElement(myarr, index, leftChildIndex);
        index = leftChildIndex;
        continue;
      } else return;
    }
    if (leftChildIndex === undefined && rightChildIndex !== undefined) {
      if (myarr[index] < myarr[rightChildIndex]) {
        swapArrayElement(myarr, index, rightChildIndex);
        index = rightChildIndex;
        continue;
      } else return;
    }

    const largerChildIndex = myarr[leftChildIndex] >= myarr[rightChildIndex] ? leftChildIndex : rightChildIndex;

    if (myarr[index] < myarr[largerChildIndex]) {
      swapArrayElement(myarr, index, largerChildIndex);
      index = largerChildIndex;
    } else return;
  }
}

for (let i = 0; i < n; i++) {
  if (dtarray[i] === 0) {
    if (dataArray.length === 0) console.log(0);
    else {
      console.log(dataArray[0]);
      dataArray.shift();
      trickleDown(dataArray, 0);
    }
  } else {
    pushNewElementToArray(dataArray, dtarray[i]);
  }
}
