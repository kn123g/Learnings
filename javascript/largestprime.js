var number = 600851475143, a = 0, p = 0;
var i;

   for( i = 2; i< number; i++) {
         while(number%i == 0) {
            number = number/i;
         }
      }
      if(number >2) {
         console.log(number);
      }
