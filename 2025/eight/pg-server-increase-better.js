function solution(players, m, k) {
  let res = 0;
  const computer = [];
  for (let i = 0; i < players.length; i++) {
    while (computer[0] === i) computer.shift(); // 종료 시각이 현재 시각과 같으면 빼버리기
    if (Math.floor(players[i] / m) > computer.length) {
      let count = Math.floor(players[i] / m) - computer.length;
      res += count;
      while (count--) computer.push(i + k);
    }
  }
  return res;
}
