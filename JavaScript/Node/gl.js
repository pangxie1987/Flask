'use strict'

console.log('current js file:'+ __filename);
console.log('current js dir:'+__dirname);
process.name = 'Sample Nodejs';
console.log('arguments:'+ JSON.stringify(process.argv));

//process.cwd()返回当前工作目录
console.log('cwd: ' + process.cwd());

//切换工作目录
var d = "C:\\Python"
if (process.platform === 'wind32'){
    //如果win32，切换到 C:\Windows\System32
    d = 'C:\\Windows\\System32'
}
process.chdir(d);
console.log('cwd: ' + process.cwd());

//process.nextTick()将在下一轮时间循环中调用
process.nextTick(function() {
    console.log('nextTick callback!');
});
console.log('nextTick was set!');

//程序即将推出的回调函数
process.on('exit', function(code){
    console.log('about to exit with code:' + code);
})

//返回当前工作目录
console.log('cwd:' + process.cwd());