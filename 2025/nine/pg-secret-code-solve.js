// n까지의 숫자를 입력받아 m 길이의 조합을 만들어주는 함수
function generateCombinations(n, m) {
  const result = [];
  function addCombination(num, cnt, arr) {
    if (cnt === m) {
      result.push([...arr]);
      return;
    }

    for (let i = num + 1; i <= n; i++) {
      arr.push(i);
      addCombination(i, cnt + 1, arr);
      arr.pop();
    }
  }

  addCombination(0, 0, []);
  return result;
}
