/*
  Generate an 0-indexed array where:
  sieve[i] = False indicates non-prime
  sieve[i] = True indicates prime
*/

const sieveOfEratosthenes = (num) => {
  let sieve = [];
  for (let i = 0; i < num; i++) {
    sieve.push(0);
  }

  sieve[0] = false;
  console.log(sieve);

  for (let i = 2; i < num + 1; i++) {
    if (sieve[i - 1] === 0) sieve[i - 1] = true;

    for (let j = i * 2; j < num + 1; j += i) {
      sieve[j - 1] = false;
    }
  }

  console.log(sieve);
  return sieve;
};

const primeMap = (arr) => {
  let result = {};

  for (let i = 0; i < arr.length; i++) {
    if (arr[i]) result[arr[i] + 1] = true;
  }

  console.log(result);
  return result;
};

const primeFactorization = (num) => {
  let primes = sieveOfEratosthenes(num);
  let result = [];
  let rem = num;

  while (rem % 2 === 0) {
    rem = rem / 2;
    result.push(2);
  }

  for (let i = 3; i < num + 1; i += 2) {
    if (primes[i - 1] === false) continue;

    while (rem % i === 0) {
      result.push(i);
      rem = rem / i;
    }

    if (rem === 1 || rem === 0) break;
  }

  console.log(result);
  return result;
};

const numberOfDivisors = (num) => {
  let primeFactors = primeFactorization(num);
  let result = 1;
  let hm = {};

  for (let i = 0; i < primeFactors.length; i++) {
    const N = primeFactors[i];

    if (hm[N]) hm[N]++;
    else hm[N] = 1;
  }

  const KEYS = Object.keys(hm);

  for (let i = 0; i < KEYS.length; i++) {
    const N = hm[KEYS[i]];
    result *= N + 1;
  }

  console.log(result);
  return result;
};

const checkPrime = (num) => {
  const SQ_RT = Math.ceil(Math.pow(num, 1 / 2));

  let isEven = false;
  if (num % 2 === 0) isEven = true;

  for (let i = 2; i <= SQ_RT; i++) {
    if (num % i === 0) return false;
    if (isEven) i++;
  }

  return true;
};
