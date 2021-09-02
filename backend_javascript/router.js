var http = require('http');
var url = require('url');
var server = http.createServer(function(req,res){
  console.log("req");
  var path = url.parse(req.url).pathname;
 if(path === '/hi' || path === "/hello" )
 {
res.writeHead(200,{"content-Type":"text/plain"});
res.write('"Hi Welcome" and "Hello Buddy" respectively.');
 }
 else{
   res.writeHead(404,{"content-Type":"text/plain"});
res.write('"404 Page not Found" response when another URL is accessed');
 }


res.end();
console.log('"Hi TCSer" "Hi Welcome" "Hello Buddy"');
console.log(' "Welcome Home"');
console.log('"HI TCSer"');
console.log('"404 File not found error"');
})
server.listen(8000);