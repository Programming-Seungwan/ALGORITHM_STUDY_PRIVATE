// 매 횟수마다 m으로 나누고, 부족한 대수만큼 증설을 한다.
// 시간이 다 지났으면 해당 서버는 이제 종료시킨다 -> 매 턴이 끝나면 시간을 늘리고, 끝난 것들은 종료시킨다.

class Server {
  constructor() {
    this.age = 0;
  }

  getAge() {
    return this.age;
  }

  addAge() {
    this.age++;
  }
}

function solution(players, m, k) {
  let serverList = [];
  let increaseCount = 0;
  for (player of players) {
    if (player >= m) {
      const neededCount = Math.floor(player / m); // 증설할 필요가 있는 서버 수 : 기존꺼까지 활용
      const increasingServerCount = neededCount - serverList.length;

      for (let i = 0; i < increasingServerCount; i++) {
        const serverInstance = new Server();
        serverList.push(serverInstance);
        increaseCount += 1;
      }
    }

    serverList.map((server) => server.addAge());
    serverList = serverList.filter((server) => server.getAge() < k);
  }
  return increaseCount;
}
