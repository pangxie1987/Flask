'use strict';

var s = 'Hello';

function hi(name){
    console.log('Hi,' + name + '!')
}

function greet(name){
    console.log(s + ',' +name+ '!');
}

function goodbye(name){
    console.log('Googbye,' + name +'!')
}

module.exports = {
    hi:hi,
    greet:greet,
    goodbye:goodbye
};

// exports.hello = hello;
// exports.greet = greet;