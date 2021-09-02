import cluster from "cluster";
import express from "express";
import {cpus} from "os";
import {fork} from "child_process";

const app = express();

const cpulength = cpus().length;

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
        cluster.worker.kill();
    })
    
});

    if(cluster.isMaster){
        for(let i =0;i<cpulength;i++){
            cluster.fork();
        }
        cluster.on("exit",(worker,code,signal)=>{
            console.log(`killed process`,worker.process.pid)
            cluster.fork();
        });
    }
    else{
        app.listen(3000,()=>console.log(`listening port 3000 by process ${process.pid}`))
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