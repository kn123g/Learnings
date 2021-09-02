

//var a = parseInt(process.argv.slice(2));
//var b= parseInt(process.argv.slice(3));
//console.log(a);
//console.log(b);
//console.log(a+b);	


//setTimeout(()=>{console.log("TCS");},2000);



var run = ()=>{console.log("TCS");};
var running = setInterval(run,2000);
	setTimeout(()=> {
		clearInterval(running);
	},10000);
	console.log(__dirname);
		console.log(__filename);