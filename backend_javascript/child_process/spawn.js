import { spawn} from "child_process";
import { stderr } from "process";

// exec and execFile are bufferreader where spawn is stream reader
console.log(process.platform)
const child =spawn('dir',[],{ shell: true });

child.stdout.on('data',data=>{
    console.log(data.toString())
})

child.stderr.on('data',stderr=>{
    console.log(stderr)
})

child.on('error',(error)=>{
    console.log(error)
})

child.on('exit',(code,signal)=>{
    if(code){
        console.log(`process exit code ${code}`)
    }
    if(signal){
        console.log(`process killed with signal ${signal}`)
    }
    console.log("Done")
})