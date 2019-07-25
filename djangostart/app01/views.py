from django.shortcuts import render,HttpResponse
from .models import UserInfo
# Create your views here.

def demo(request):


    # return HttpResponse('helloworld')
    return render(request, 'app01/demo01.html')

def demo_form(request):



    username = request.GET.get("email")
    password = request.GET.get("password")

    return render(request,'app01/demo02_form.html',{"user":username})

def demo_form2 (request):
    userlist = {"a@a.com": "123123"}
    msg = ""
    if request.method == "POST":
        username =  request.POST.get("email")
        password = request.POST.get("password")
        if username in userlist and password == userlist[username]:
            return HttpResponse(f"<h2>欢迎您，{username}</h2>")
        else:
            msg = '用户名或密码错误'
    kwgs = {
        "msg":msg,
    }
    return render(request,'app01/demo02_form2.html',kwgs)


def demo_form_db (request):
    msg = ""
    # userlist = UserInfo.objects.all()
    # print(userlist)
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        result = UserInfo.objects.filter(email=username)
        if result and result[0].password == password:
            return HttpResponse(f"<h2>欢迎您，{username}</h2>")
        else:
            msg = '用户名或密码错误'
    kwgs = {
        "msg":msg
    }
    return render(request,'app01/demo02_form_db.html',kwgs)