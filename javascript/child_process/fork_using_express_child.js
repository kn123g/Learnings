function runChild(){
    let sum =0;
    for (let i=0;i<1e9;i++){
        sum = sum + i;
    }
    return sum;
}

process.send(runChild())

console.log(`child process id`,process.pid)
console.log(`child process parent id`,process.ppid)
