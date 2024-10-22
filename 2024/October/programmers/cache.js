function isThereCityInCache(cacheArr, cityName) {
  for (const element of cacheArr) {
    if (element === cityName) return true;
  }

  return false;
}

function solution(cacheSize, cities) {
  if (cacheSize === 0) {
    return 5 * cities.length;
  }
  // 캐시 사이즈에 맞춰서 큐로 사용할 배열을 만들어놓는다.
  const cache = new Array(cacheSize).fill(null);
  // 실행시간을 만든다
  let executionTime = 0;
  for (const city of cities) {
    const lowerCity = city.toLowerCase();
    if (!isThereCityInCache(cache, lowerCity)) {
      cache.shift();
      cache.push(lowerCity);
      executionTime += 5;
    } else {
      const cacheIndex = cache.indexOf(lowerCity);
      cache.splice(cacheIndex, 1);
      cache.push(lowerCity);
      executionTime += 1;
    }
  }

  return executionTime;
}

console.log(
  solution(3, [
    'Jeju',
    'Pangyo',
    'Seoul',
    'NewYork',
    'LA',
    'Jeju',
    'Pangyo',
    'Seoul',
    'NewYork',
    'LA',
  ])
);

console.log(
  solution(3, [
    'Jeju',
    'Pangyo',
    'Seoul',
    'Jeju',
    'Pangyo',
    'Seoul',
    'Jeju',
    'Pangyo',
    'Seoul',
  ])
);
