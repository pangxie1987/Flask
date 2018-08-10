
//1、在本目录下执行 npm i koa
//2、建立package.json文件  然后执 npm install

const Koa = require('koa');

const app = new Koa();

app.use(async (ctx, next) => {
    await next();
    //设置response的Content-Type;
    ctx.response.type = 'text/html';
    //设置response的内容
    ctx.response.body = '<h1>Hello, koa2!</h1>';
});

//处理paht='/'的请求
app.use(async (ctx, next) => {
    if (ctx.request.paht ==='/'){
        ctx.response.type = 'text/html';
        ctx.response.body = '<h1>In Path /</h1>';
    }else{
        await next();
    }
});

app.use(async (ctx, next) => {
    if (ctx.request.paht === '/test') {
        ctx.response.type = 'text/html';
        ctx.response.body = '<h1>In Path test</h1>';
    }else {
        await next();
    }
});

app.use(async (ctx, next) => {
    if (ctx.request.paht === '/error') {
        ctx.response.type = 'text/html';
        ctx.response.body = '<h1>In Path error</h1>';
    } else {
        await next();
    }
});

app.use(async (ctx, next) => {
    console.log(`${ctx.request.method} ${ctx.request.url}`); //打印url
    await next(); //调用下一个middleware
});

app.use(async (ctx, next) => {
    const start = new Date().getTime(); //当前时间
    await next();
    const ms = new Date().getTime()-start; //消耗时间
    console.log(`Time: ${ms}ms`); //打印消耗时间
});

app.listen(3000);
console.log('app started at port 3000...');