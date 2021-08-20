import express from "express";
import {fork} from "child_process";
const app = express();

app.get(`/one`,(req,res)=>{
    res.send({msg:longCompute()});
});
app.get(`/two`,async (req,res)=>{
    res.send({msg:await longComputePromise()});
});
app.get(`/three`,(req,res)=>{
    console.log(`parent process id`,process.pid)
    console.log(`parent process parent id`,process.ppid)
    const child = fork("./fork_using_express_child.js");
    child.on("message",msg=>{
        res.send({msg:msg});
    })
});
app.listen(3000,()=>console.log(`server on port 3000`));

function longCompute(){
    let sum =0;
    for (let i=0;i<1e9;i++){
        sum = sum + i;
    }
    return sum;
}

function longComputePromise(){
    return new Promise((resolve,reject) => {
        try{
            let sum = 0;
            for (let i=0;i<1e9;i++){
                sum = sum + i;
            }
            resolve(sum);
        }catch(e){
            reject(0);
        }
    });
}
