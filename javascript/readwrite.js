var fs =require("fs");
var write = fs.createWriteStream("output.txt");
write.write("Node.js is an ultimate backend javascript for backend development","utf8");
write.end();
write.on("finish",()=>{

});


//copy
var fs =require("fs");

var read = fs.createWriteStream( process.cwd()+ "/Node-stream-handson/data_file.txt");
var write = fs.createWriteStream( process.cwd()+ "/new_data_file.txt");

read.pipe(write);