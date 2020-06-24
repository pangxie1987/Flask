//负责真正启动应用
//test: npm test

const app = require('./app');

app.listen(3000);
console.log('app started at port 3000...');