from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404 , JsonResponse
from .models import mark ,student ,teacher,login
import json 
login_data = login.objects.all()
# Create your views here.
def homepage(request):
    return HttpResponse("hello")
def loginpage(request):

    if request.method == 'POST':
        
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        username = data["username"]
        password = data["password"]
        for un in login_data:
            if username == un.username:
                
                if password == un.password:
                    t ="logged in" 
                    a=(un.username)
                    b=(un.password)
                    x={
                        "a":a,"b":b,"o":t
                    }
                    y= json.dumps(x)
                    break
                else:
                    y="give correct password"
            else:
                t="give correct input" 
                a=(un.username)
                b=(un.password)
                x={
                    "a":a,"b":b,"o":t
                }
                y= json.dumps(x)
    return HttpResponse(y)
          # x="a"
        # uname = login.username
        # passw = login.password


        
        # y="both username and password is wrong"

        # # data=json.loads(request.body)
        # # username = json.JSONDecoder(data)

        # print(type(data))
        
    #     data= hello
    #     print(data)

    
    #     # username=request.POST.get('username')
        # print(username)
def addstudent(request):
    if request.method =="POST":
    
        body_unicode = request.body.decode('utf-8')
        k = json.loads(body_unicode)
       
        teacher.objects.create(**k)
        r={"data":k,"status":"ok" } 
        y=json.dumps(r)
    return HttpResponse(y)
def seedetails(request):
    if request.method == "POST":
        teacher_data = list(teacher.objects.all().values())
    return JsonResponse(teacher_data , safe= False)
