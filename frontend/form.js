function takeinput(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    myobj={username: username, password: password} ;
    data= JSON.stringify(myobj);
    console.log(data)

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:8000/home/login/",true);
    xhttp.onreadystatechange = function()
    {

        console.log(xhttp.readyState)
        
        
        xhttp.onload = function(){
            if(this.readyState==4 && this.status === 200){
            console.log(this.responseText)
            document.getElementById("return").innerHTML = this.responseText;
              
        }
        else{
            console.log ("some error occured")
        }
    }
    };
    
    xhttp.send(data)
    console.log(myobj)

}
