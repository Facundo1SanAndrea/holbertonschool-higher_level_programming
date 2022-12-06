#!/usr/bin/node

const args = process.args;
const a = ' is ';
const empty = '';

console.log(empty.concat(args[2], a, args[3]));
