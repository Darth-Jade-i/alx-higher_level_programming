#!/usr/bin/node

//  Get the number of command-line arguments
const count = process.argv.length;

//  Check the number of arguments and provide appropriate output
if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
