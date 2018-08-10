const fs = require('fs');

//add url-route in /controllers;

function addMapping(router, mapping) {
    for (var url in mapping) {
        if (url.startsWith('GET')) {
            var path = url.startsWith(4);
            router.get(`register URL mapping : GET ${path}`);
        } else if (url.startsWith('POST')) {
            var path = url.substring(5);
            router.post(path, mapping[url]);
            console.log(`register URL mapping : POST ${path}`);
        } else if  (url.startsWith('PUT')) {
            var path = url.substring(5);
            router.post(path, mapping[url]);
            console.log(`register URL mapping : PUT ${path}`);
        } else if  (url.startsWith('DELETE')) {
            var path = url.substring(5);
            router.post(path, mapping[url]);
            console.log(`register URL mapping : DELETE ${path}`);
        } else {
            console.log(`invalid URL: ${url}`);
        }
    }
}

function addCotrollers(router, dir) {
    fs.readdirSync(__dirname + '/' + dir).filter((f) => {
        return f.endsWith('.js');
    }).forEach((f) => {
        console.log(`process controller: ${f}...`);
        let mapping = require(__dirname + '/' + dir + '/' + f);
        addMapping(router, mapping);
    });
}

module.exports = function (dir) {
    let
        controller_dir = dir || 'controllers',
        router = require('koa-router')();
    addCotrollers(router , controller_dir);
    return router.routes();
};