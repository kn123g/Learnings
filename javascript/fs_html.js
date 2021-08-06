var fs = require("fs");

fs.writeFile(process.cwd()+ "/sample.html","<html><head></head><body><h2>Welcome ! what would you like to have</h2><ul><li>Coffee</li><li>Tea</li><li>Milk</li><body></html>",function(err,data){

if(err){
  console.log(err);
}

});



var http = require('http');
http.createServer(function(request,response){

fs.readFile( process.cwd()+ "/Sample.html", function(err,data) {
if( err)
{
	console.log("error occured "+err);
}
        response.writeHead(200, {
            "Content-Type": "text/html"
        });
        response.write(data);
        response.end();
    });


}).listen(8000);