// 어떤 자료 구조를 사용해야 연산자들 간의 우선 순위를 적용하여 계산을 진행할 수 있을지 고민
// 피연산자와 연산자로 나눠놓은 배열을 구해준다.
// 우선 순위에 맞게 배열을 순회하며 이를 계산해서 진행해준다.
// 연산자는 +, -, * 3개로 이루어진다.
// 우선 순위는 총 6가지 케이스를 점검해야한다.
// 문자열을 -, *, +로 나누어서 배열로 저장하는 함수를 만들기
function splitExpression(expression) {
  const result = [];
  let currentNumber = ''; // 숫자를 의미

  for (let tmpChar of expression) {
    if (tmpChar === '*' || tmpChar === '+' || tmpChar === '-') {
      if (currentNumber.length !== 0) {
        result.push(currentNumber);
        currentNumber = '';
      }
      result.push(tmpChar);
    } else {
      currentNumber += tmpChar;
    }
  }

  if (currentNumber) {
    result.push(currentNumber);
  }

  return result;
}

const priorityArray = [
  ['+', '-', '*'],
  ['+', '*', '-'],
  ['-', '+', '*'],
  ['-', '*', '+'],
  ['*', '-', '+'],
  ['*', '+', '-'],
];

function calculateWithPriority(copiedArray, priorityArr) {
  for (let operand of priorityArr) {
    while (true) {
      const operandIndex = copiedArray.indexOf(operand);
      if (operandIndex === -1) {
        break;
      }

      const beforeValue = parseInt(copiedArray[operandIndex - 1]);
      const afterValue = parseInt(copiedArray[operandIndex + 1]);
      const tmpCalValue =
        operand === '*'
          ? beforeValue * afterValue
          : operand === '+'
          ? beforeValue + afterValue
          : beforeValue - afterValue;
      copiedArray.splice(operandIndex - 1, 3, tmpCalValue);
    }
  }

  return Math.abs(copiedArray[0]);
}

function solution(expression) {
  const resultValueArray = []; // 계산 결과를 수행한 값들을 넣어놓을 배열
  const splitedExpressionArray = splitExpression(expression); // 원본 배열이니까 훼손시키면 안됨

  for (const tmpPriorityArr of priorityArray) {
    resultValueArray.push(
      calculateWithPriority([...splitedExpressionArray], tmpPriorityArr)
    );
  }

  return Math.max(...resultValueArray);
}
