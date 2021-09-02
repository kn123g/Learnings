import {execFile} from "child_process";

execFile("dir.bat",(err,stdout,stderr)=>{
    if(err){
        console.log(err)
        return ;
    }
    if(stderr){
        console.log(stderr)
        return ;
    }
    console.log(stdout)
})