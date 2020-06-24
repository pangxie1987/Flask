'use strict';

// //文件服务器
// var url = require('url');
// //处理url
// console.log(url.parse('http://user:pass@host.com:8080/path/to/file?query=string#hash'));

// //处理本地文件目录
// var path = require('path');

// //解析当前目录
// var workDir = path.resolve();
// console.log('workDir:' + workDir);

// //组合完成的文件路径：当前目录+'pub'+'index.html'
// var filepath = path.join(workDir, 'pub', 'index.html');

// console.log('filepath:' + filepath)

//文件服务器

var 
    fs = require('fs'),
    url = require('url'),
    path = require('path'),
    http = require('http');

//从命令行参数获取root目录，默认是当前目录
var root = path.resolve(process.argv[2] || '.');

console.log('Static root dir: '  + root);

//创建服务器
var server = http.createServer(function(request, response){
    //获取url的path
    var pathname = url.parse(request.url).pathname;
    //获取对应的本地路径
    var filepath = path.join(root, pathname);

    //读取文件状态
    fs.stat(filepath, function(err, stats){
        if (!err && stats.isFile()){
            //没有出错并且文件存在
            console.log('200', request.url);

            //发送200响应
            response.writeHead(200);
            //将文件流导向response
            fs.createReadStream(filepath).pipe(response);
        } else if (!err && stat.isDirectory()){
            console,log(fs.readdir(filepath, 'utf-8', function(err, files){
                if (err){
                    console.log(err);
                }else{
                    for (let file of files){
                        if (file=='index.html' || file == 'default.html'){
                            console.log('200:' + request.url);
                            response.writeHead(200);
                            fs.createReadStream(path.join(filepath, file)).pipe(response);
                        }
                    }
                }
            }))
        }
        
        else {
            //出错了或者文件不存在
            console.log('404', + request.url);
            //发送404响应
            response.writeHead(404);
            response.end('404 Not Found');
        }

        
    });
});

server.listen(8080);
console.log('Server is running at http://127.0.0.1:8080/');