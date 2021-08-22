let x =new XMLHttpRequest();
let countries = null;

x.onload = function (){
  if(this.status >= 200 && this.status <= 200){
    countries = JSON.parse(this.responseText);
    for(let i=0;i<countries.length;i++)
        console.log(`%c${countries[i].name}`,'color: #ea146a')
    for(let country in countries)
      console.log(`%c${countries[country].name}     %c${countries[country].region}`,'color: #ea146a','color: #15d853')
    for(let country of countries)
    console.log(`%c${country.name}    %c${country.region}   %c${country.nativeName}`,'color: #ea146a','color: #15d853','color: #000000')
    countries.forEach(element => {
      console.log(`%c${element.name}    %c${element.region}   %c${element.nativeName}`,'color: #ea146a','color: #15d853','color: #000000')
    });
  }
}

x.onerror = function(){
  console.log(this.statusText);
}

x.open('GET','https://restcountries.eu/rest/v2/all');
x.send();


