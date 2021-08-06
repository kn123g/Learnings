var MyEvent= require('events');
var e = new MyEvent.EventEmitter();
var e1 = new MyEvent.EventEmitter();
var Myfunc = ()=> {

console.log('HI THERE ! HAPPY LEARNING');

};

e.on('MyEvent',Myfunc);
e.emit('MyEvent');
