'use strict'

var fs = require('fs');

//异步读取文件
fs.readFile('sample.txt','utf-8',function(err,data){
    if (err){
        console.log(err);
    }else{
        console.log(data);
    }
});

//异步读取图片
fs.readFile('sample.jpg', function(err, data){
    if (err){
        console.log(err);
    }else{
        console.log(data);
        console.log(data.length + ' bytes');
    }
});


//同步读文件
try {
    var data = fs.readFileSync('sample.txt', 'utf-8');
    console.log(data);
} catch(err){
    console.log('something is wrong!')
}

//异步写文件
var data = 'async Hello Node.js';
fs.writeFile('output.txt', data, function(err){
    if (err){
        console.log(err);
    } else{
        console.log('write Sucess!');
    }
});

//同步写文件
var data = 'Sync Write to File!';
fs.writeFileSync('output.txt', data);

//异步读取文件信息（文件大小，创建时间等）
fs.stat('sample.txt', function(err, stat){
    if (err){
        console.log(err);
    } else{
        //是否是文件
        console.log('isFile: ' + stat.isFile());
        if (stat.isFile()){
            //文件大小
            console.log('size: '+stat.size);
            //创建时间，date对象
            console.log('birth time: '+ stat.birthtime);
            //修改时间，date对象
            console.log('modified time: '+ stat.mtime);
        }
    }
});

//同步读取文件信息
try {
    var info = fs.statSync('sample.txt');
    console.log('File size:'+ info.size);
} catch (err){
    console.log('File message read fail')
}
