const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')[0];

const stack = [];
let result = 0;

for (let i = 0; i < input.length; i++) {
  if (input[i] === '(') {
    stack.push('(');
  } else {
    stack.pop();
    if (input[i - 1] === '(') {
      result += stack.length;
    } else {
      result += 1;
    }
  }
}

console.log(result);
