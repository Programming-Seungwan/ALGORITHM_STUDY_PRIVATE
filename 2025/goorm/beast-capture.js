// Run by Node.js
const readline = require('readline');

// 덫이 유효 범위 내에 있는지를 판단하는 함수
function availableTrick(bx, by, gx, gy, tx, ty) {
  const isAvailableTx = (bx >= tx && tx >= gx) || (bx <= tx && tx <= gx);
  const isAvailableTy = (by >= ty && ty >= gy) || (by <= ty && ty <= gy);

  return isAvailableTx && isAvailableTy;
}

function getDistance(x1, y1, x2, y2) {
  const dx = x2 - x1;
  const dy = y2 - y1;
  return Math.sqrt(dx * dx + dy * dy);
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  const inputArray = [];

  for await (const line of rl) {
    inputArray.push(line.split(' ').map((num) => parseInt(num)));
    rl.close();
  }
  const b = inputArray[0];
  const g = inputArray[1];
  const N = inputArray[2][0];
  const trickArray = inputArray.slice(3);

  if (getDistance(b[0], b[1], g[0], g[1]) < 5) {
    console.log('NO');
    return;
  }

  let availableCount = 0;

  for (const trick of trickArray) {
    if (availableTrick(b[0], b[1], g[0], g[1], trick[0], trick[1])) {
      availableCount += 1;
    }
  }

  if (availableCount >= 3) {
    console.log('YES');
  } else {
    console.log('NO');
  }

  process.exit();
})();
