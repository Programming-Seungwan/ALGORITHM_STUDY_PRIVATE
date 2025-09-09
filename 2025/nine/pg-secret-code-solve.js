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

// n은 최대 숫자, q는 시도해본 배열, ans는 그에 대한 결과임
function solution(n, q, ans) {
  let combinations = generateCombinations(n, 5);

  for (let i = 0; i < q.length; i++) {
    const querySet = new Set(q[i]);

    combinations = combinations.filter((comb) => {
      let match = 0;
      for (const num of comb) {
        if (querySet.has(num)) match++;
      }

      return ans[i] === match;
    });
  }

  return combinations.length;
}
