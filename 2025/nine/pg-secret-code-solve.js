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
    } // 특정 요소를 밀어넣고, 다시 빼는 것이 backtracking 알고리즘의 핵심
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
        // 구한 조합의 특정 요소가 테스트케이스마다 산출된 결과와 매번 일치하면 해당 조합은 남겨둔다.
        if (querySet.has(num)) match++;
      }

      return ans[i] === match; // 점검이 끝난 뒤 조건을 검사하여 해당 comb를 남길지 검사
    });
  }

  return combinations.length;
}
