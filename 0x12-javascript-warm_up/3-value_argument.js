#!/usr/bin/node

// Check if the command-line argument at index 2 is undefined
if (typeof process.argv[2] === 'undefined') {
  // If undefined, log 'No argument'
  console.log('No argument');
} else {
  // If argument is defined, log the value of process.argv[2]
  console.log(process.argv[2]);
}
