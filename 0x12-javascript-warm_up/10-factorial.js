#!/usr/bin/node
const a = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 2) {
    return 2;
  } else {
    return n * factorial(n - 1);
  }
}

if (isNaN(a)) {
  console.log(1);
} else {
  const f = factorial(a);
  console.log(f);
}
