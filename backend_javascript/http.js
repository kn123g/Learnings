var http = require('http');
http.createServer(function(req,res){
	console.log("req");
res.writeHead(200,{"content-Type":"text/plain"});
res.write("Hello World");
res.end();
}).listen(8000);

var http = require('http');
var url = require('url');
var server = http.createServer(function(req,res){
	console.log("req");
res.writeHead(200,{"content-Type":"text/plain"});
res.write("Hello World");
res.end();
})
server.listen(8000);



