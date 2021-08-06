var sum= 0;
var fun3=()=>{
let i,n3=0;
for (i=3;i<1000;i=i+3){
n3 = n3+i;
}
return n3;

}
var fun5=()=>{
let j,n5=0;
for (j=5;j<1000;j=j+5){
n5 = n5+j;
}
return n5;

}


function calculate (fun6,fun10){
	//console.log(fun6());
	//console.log(fun10());
  sum = sum + fun6() + fun10();
  return sum;
}
console.log(calculate(fun3,fun5));
