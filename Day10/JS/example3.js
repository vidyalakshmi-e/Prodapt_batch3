let marks=[85,42,76,91,38,67,55,29,80,49];
var t_pass=0;
var t_fail=0;
var high=marks[0];
var low=marks[0];

for (var i=0;i<10;i++){
    if(marks[i] >=50){
        t_pass++;
        console.log("Student "+i+": "+marks[i]+" Pass")
    }
    else{
        t_fail++;
        console.log("Student "+i+": "+marks[i]+" - Fail")
    }
    if(marks[i]>high){
        high=marks[i];
    }
    if(marks[i]<low){
        low=marks[i];
    }
}
console.log("Total Passed: "+t_pass);
console.log("Total Failed: "+t_fail);
console.log("Highest Score: "+high);
console.log("Lowest Score: "+low);
