import {fork} from "child_process";

const child = fork("child.js",["from_karthi"]);

child.on("message",msg=>{
    console.log('child id : ',msg.processid);
    child.send({parent_processid:process.pid})
})

child.on('close',()=>{
    console.log("closing parent")
})