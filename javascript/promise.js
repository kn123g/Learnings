let stocks = {
    fruits:['straberry','grapes','banana','apple'],
    liquid:['water','ice'],
    holder:['cone','cup','stick'],
    toppings:['chocolate','peanuts']
  };
  
  let is_Shop_Open = true;
  
  let order =(time,work)=>{
    return new Promise((resolve,reject)=>{
      if(is_Shop_Open){
        setTimeout(()=>{
          resolve(work())
        },time);
      }
      else{
        reject(console.log('our shop is closed'))
      }
    })
  };
  order(2000,()=> console.log(`${stocks.fruits[0]} was selected`))
  .then(()=>{
     return order(0000,()=>console.log('production has started'))
  }
  ).then(()=>{
     return order(2000,()=>console.log('the fruit was chopped'))
  }
  ).then(()=>{
    return order(1000,()=>console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} was selected`))
  }).then(()=>{
    return order(1000,()=>console.log(`start the machine`))
  }
  ).then(()=>{
    return order(2000,()=>console.log(`icecream placed on ${stocks.holder[0]}`))
  }
  ).then(()=>{
    return order(3000,()=>console.log(`${stocks.toppings[0]} was selected`))
  }
  ).then(()=>{
    return order(1000,()=>console.log(`ice cream was served`))
  }
  ).catch(()=>{
     console.log('Customer left')
  }).finally(()=>{
    console.log('day ended, shop is closed');
  });
  
  //change is_Shop_Open variable value alternatively to test resolve and reject
  //finally will be executed every time , not bother about resolve or reject