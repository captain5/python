from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog import models
import json
# Create your views here.

def index(request):
    return HttpResponse("恭喜登陆成功！欢迎光临传智播客！")

def login(request):
    context = {"status": 'ok'}
    if request.method == "POST":
        user = models.user.objects.get(username='zhang')
        username = user.username
        passwd = user.password
        print(username,passwd)
        
        userName = request.POST.get('username', None)
        pwd = request.POST.get('pwd', None)
        print(userName, pwd)
        if userName == username and pwd == passwd:
            return HttpResponse(json.dumps(context))
        else:
            context['status'] = 'error'
            return HttpResponse(json.dumps(context))
    return render(request, 'login.html')