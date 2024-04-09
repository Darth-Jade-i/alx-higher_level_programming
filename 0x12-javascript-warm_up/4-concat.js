#!/usr/bin/node

// Get the first command-line argument (index 2) and store it in a variable
const arg1 = process.argv[2];

// Get the second command-line argument (index 3) and store it in a variable
const arg2 = process.argv[3];

// Check if both arguments are provided
if (arg1 !== undefined && arg2 !== undefined) {
  // If arguments are defined, concatenate them into a string
  console.log(arg1 + ' is ' + arg2);
} else {
  // If any argument is missing, log an appropriate message
  console.log('Insufficient arguments provided');
}
