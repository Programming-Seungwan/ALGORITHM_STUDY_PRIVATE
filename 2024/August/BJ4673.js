// function getResult(number) {
//   const tenThousandRemain = Math.floor(number / 10000);
//   const thousandRemain = Math.floor((number - (tenThousandRemain * 10000)) / 1000);
//   const hundredRemain = Math.floor((number - (tenThousandRemain * 10000) - (thousandRemain * 1000)) / 100);
//   const tenRemain = Math.floor((number - (tenThousandRemain * 10000) - (thousandRemain * 1000) - (hundredRemain * 100)) / 10);
//   const oneRemain = number % 10;

//   return number + tenThousandRemain + thousandRemain + hundredRemain + tenRemain + oneRemain
// }

function getResult(number) {
  let result = number;
  const strNumber = String(number)
  for (let i = 0; i < strNumber.length; i++) {
    result += Number(strNumber[i])
  }

  return result
}

const resultArray = new Array(10001).fill(false)

for (let i = 1; i <= 10001; i++) {
  const result = getResult(i);
  resultArray[result] = true;
}

for (let i = 1; i <= 10001; i++) {
  if (resultArray[i] === false) {
    console.log(i);
  }
}