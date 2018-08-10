'use strict'
//流

//从文件流读取数据
 var fs = require('fs');

 //打开一个流

 var rs = fs.createReadStream('sample.txt' , 'utf-8');
 rs.on('data', function(chunk){
     console.log('DATA');
     console.log(chunk);
 });

 rs.on('end', function(){
     console.log('END');
 });

 rs.on('error', function(err){
     console.log('ERROR:' +err);
 });


 //以流的形式写入文件，只需不断调用write()方法，最后以end()结束

var ws1 = fs.createWriteStream('output.txt', 'utf-8');
ws1.write('使用stream写入文本数据。。。\n');
ws1.write('END.');
ws1.end();

var ws2 = fs.createWriteStream('output2.txt');
ws2.write(new Buffer('使用stream写入二进制数据...\n', 'utf-8'));
ws2.write(new Buffer('END.', 'utf-8'));
ws2.end();
