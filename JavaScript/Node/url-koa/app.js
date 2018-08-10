
//1、在本目录下执行 npm i koa
//2、建立package.json文件  然后执 npm install
//使用koa-router处理不同的URL请求


const Koa = require('koa');

//注意require(koa-router)返回的是函数
const router = require('koa-router')();
const bodyparser = require('koa-bodyparser');
const app = new Koa();

app.use(bodyparser());

//登录表单
router.get('/', async (ctx, next) => {
    ctx.response.body = `<h1>Index</h1>
    <form action="/signin" method = "post">
        <p>Name: <input name="name" value="koa"></p>
        <p>Password: <input name="password" type="password"></p>
        <p><input type="submit" value="Submit"></p>
    </form>`;
});

router.post('/signin', async (ctx, next) => {
    var 
        name = ctx.request.body.name || '',
        password = ctx.request.body.password || '';
    console.log(`signin with name:${name}, password:${password}`);
    if (name === 'koa' && password === '12345') {
        ctx.response.body = `<h1>Welcome, ${name}!</h1>`;
    } else {
        ctx.response.body = `<h1>Login failed!</h1>
        <p><a href = "/" Try again</a></p>`;
    }
});

//log request URL;
app.use(async (ctx, next) => {
    console.log(`${ctx.request.method} ${ctx.request.url}`); //打印url
    await next(); //调用下一个middleware
});

// add url-route;
router.get('/home/:name', async (ctx, next) => {
    var name = ctx.params.name;
    ctx.response.body = `<h1>Hello, ${name}!</h1>`;
});



//add router middleware;
app.use(router.routes());

app.listen(3000);
console.log('app started at port 3000...');