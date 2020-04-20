var xmlhttp = new XMLHttpRequest();
var Student;
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    Student = JSON.parse(this.responseText);

        var html = '<ul>';
        for (i in Student)
        {
              for(k in Student[i])
             {
            html = '<l>' + Student[i] + "  :   " + Student[i][k] + '</l>'  ;
        }
   
        }
        html += '</ul>'
        console.log(html);
          document.getElementById("demo").innerHTML = html;
     }
};
xmlhttp.open("GET", "StudentsData.json", true);
xmlhttp.send();
