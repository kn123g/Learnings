//debugger;
var Student1 ={"name" : "karthikeyan",
"Age":"23",
"Subject":["English",
            "Tamil",
            "Maths",
            "Science",
            "Social"],
"Projects" : [{"01":"AI"},
            {"02":"IOT"}]
};
var Student =[{"name" : "karthikeyan",
"Age":"23",
"Subject":["English",
            "Tamil",
            "Maths",
            "Science",
            "Social"],
"Projects" : [{"01":"AI"},
            {"02":"IOT"}]
},
{"name" : "kavi",
"Age":"22",
"Subject":["English",
            "Tamil",
            "Maths",
            "Science",
            "Social"],
"Projects" : [{"A01":"AI"},
            {"B02":"IOT"}]
}];

for (i=0;i<Student.length;i++)
{
    console.log(Student[i].name);
    console.log(Student[i].Age);
    for (j=0;j<Student[i].Subject.length;j++){
           console.log(Student[i].Subject[j]);
        
    }
    for (k=0;k<Student[i].Projects.length;k++){
        for (projectkey in Student[i].Projects[k]){
           console.log(projectkey);
        }
    }

}

console.log("\n\n");


for (i in Student)
{
    console.log(Student[i].name);
    console.log(Student[i].Age);
    for (j in Student[i].Subject){
           console.log(Student[i].Subject[j]);
        
    }
    for (k in Student[i].Projects){
        for (projectkey in Student[i].Projects[k]){
           console.log(Student[i].Projects[k][projectkey]);
        }
    }
}
for (i in Student1)
{
    console.log(Student1[i]);
}