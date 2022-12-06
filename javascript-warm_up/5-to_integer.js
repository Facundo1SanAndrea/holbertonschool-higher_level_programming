#!/usr/bin/node
/*TASK 5*/ 
import { argv } from 'node:process';

if (parseInt(argv[2])) {
    console.log('My number: %d', parseInt(argv[2]));
} else {
    console.log('Not a number');
}