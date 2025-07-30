// Run by Node.js
const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    const [ab, ac] = line.split(' ').map((el) => +el);
    if (ab === ac) {
      console.log('1 : 1');
      return;
    }
    const biggerNumber = ab > ac ? ab : ac;
    const smallerNumber = ab < ac ? ab : ac;
    const biggestDividingNum = smallerNumber;

    for (let i = smallerNumber; i >= 1; i--) {
      if (biggerNumber % i === 0 && smallerNumber % i === 0) {
        console.log(`${biggerNumber / i}:${smallerNumber / i}`);
        return;
      }
    }
    rl.close();
  }

  process.exit();
})();
