//返回一个随机数

http = require('http');
url = require('url');

http.createServer(function(request, response) {
    response.writeHead(200, {"Contont-Type":'text/plain'});
    var params = url.parse(request.url, true).query;
    var input = params.number;
    var numInput = new Number(input);
    var numOutput = new Number(Math.random()*numInput).toFixed(0);
    response.write(numOutput);
    response.end();
}).listen(80);

console.log("Random Number Generator running...")