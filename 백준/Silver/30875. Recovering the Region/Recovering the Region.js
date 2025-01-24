const fs = require('fs');

// Read input
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let [n, ...arr] = input;
n = +n;
// // Initialize maps and arrays

  for (let i = 0; i < n; i++) {
    console.log(Array(n).fill(i + 1).join(' '));
  }

