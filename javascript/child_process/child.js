process.on("message",(msg)=>{
    console.log("parent_processid",msg.parent_processid)
})

console.log("hai",process.argv[2]);

process.send({processid:process.pid})

process.send('close')
