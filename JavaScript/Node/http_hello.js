'use strict'

//创建第一个服务器
var http = require('http');

//创建http server并传入回调函数
var server = http.createServer(function(request, response){
    //回调函数接收request和response对象
    //获得HTTP请求的method和url
    console.log(request.method + ':' +request.url);
    //将HTTP响应的200写入response,同时设置Content-Type:text/html;
    response.writeHead(200,{'Content-Type' : 'text/html'});
    //将HTTP响应的HTML内容写入response；
    response.end('<h1>Hello World!</h1>');
});

//让服务器监听8080端口
server.listen(8080);

console.log('Server is running a t http://localhost:8080/');

