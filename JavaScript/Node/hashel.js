//哈希加密算法

//MD5
const crypto = require('crypto');
const hash = crypto.createHash('md5');

//可任意多次调用update();
hash.update('Hello, World!');
hash.update('Hello, Node!');
console.log(hash.digest('hex'));

//使用sha1
const hash1 = crypto.createHash('sha1');
//可任意多次调用update();
hash1.update('Hello, World!');
hash1.update('Hello, Node!');
console.log(hash1.digest('hex'));