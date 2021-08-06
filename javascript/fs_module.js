var fs = require("fs");
fs.mkdirSync(process.cwd()+ "/Node_folder",{recursive:true},(error)=>
{
if(error)
{
console.log(error);
}
});
fs.writeFile(process.cwd()+ "/Node_folder/sample.txt","This is Node.js a powerful backend javascript used very widely in industry for developing web applications",function(err,data){

if(err){
  console.log(err);
}

});