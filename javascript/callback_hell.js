let stocks = {
    fruits:['straberry','grapes','banana','apple'],
    liquid:['water','ice'],
    holder:['cone','cup','stick'],
    toppings:['chocolate','peanuts']
  };
  
  stocks.fruits[2]
  let  order = (fruit_name,production)=> {
    setTimeout(()=>{
      console.log(`${stocks.fruits[fruit_name]} was selected`)
      production();
    },2000);
  }
  let  production =  ()=>{
    setTimeout(()=>{
      console.log('production has started')
      setTimeout(()=>{
        console.log('the fruit has been chopped')
        setTimeout(()=>{
          console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} was added`)
          setTimeout(()=>{
            console.log('the machine was started')
            setTimeout(()=>{
              console.log(`icecream was placed on cone ${stocks.holder[0]}`)
              setTimeout(()=>{
                console.log(`${stocks.toppings[0]} was added as toppings`)
                setTimeout(()=>{
                  console.log(`serve icecream`)
    
                },2000);
              },3000);
            },2000);
          },1000);
        },1000);
      },2000);
    },0);
  }
  order(0,production);
  //call hell difficult to understand so, need to use promise                   