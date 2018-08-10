'use strict'

//pipe将读取和写入流串起来（实际上达到了copy文件的效果）
const fs = require('fs');

var rs = fs.createReadStream('sample.txt');
var ws = fs.createWriteStream('copied.txt');

rs.pipe(ws);