const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const stack = [];
let result = '';

for (let i = 1; i < input.length; i++) {
  const [command, value] = input[i].trim().split(' ');

  switch (command) {
    case 'push':
      stack.push(value);
      break;
    case 'pop':
      result += (stack.pop() || -1) + '\n';
      break;
    case 'size':
      result += stack.length + '\n';
      break;
    case 'empty':
      result += (stack.length === 0 ? 1 : 0) + '\n';
      break;
    case 'top':
      result += (stack[stack.length - 1] || -1) + '\n';
      break;
  }
}

console.log(result);
