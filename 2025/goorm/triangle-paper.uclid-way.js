// Run by Node.js
const readline = require('readline');

function gcd(a, b) {
  while (b !== 0) {
    [a, b] = [b, a % b];
  }
  return a;
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    const [ab, ac] = line.split(' ').map((el) => +el);
    if (ab === ac) {
      console.log('1:1');
    } else {
      const dividingNumber = gcd(ab, ac);

      console.log(`${ab / dividingNumber}:${ac / dividingNumber}`);
    }

    rl.close();
  }

  process.exit();
})();
