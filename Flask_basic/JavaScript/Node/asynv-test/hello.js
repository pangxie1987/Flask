//待测试文件  mocha的异步测试

const fs = require('mz/fs');

//a sample async function;
module.exports = async () => {
    let expression = await fs.readFile('./data.txt' , 'utf-8') ;
    let fn = new Function('return ' + expression);
    let r = fn();
    console.log(`Caculate: ${expression} = ${r}`);
    return r;
};