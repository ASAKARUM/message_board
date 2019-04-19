from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django import forms
from .forms import UserForm
from .models import Post, Record
import datetime
#from django import HttpResponseRedirect
#from django.core.urlresolvers import reverse

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            register_data = User.objects.create_user(username=username, password=password)
            if register_data == True:
                return render(request, 'regmsg.html', {'register_data': register_data, 'username': username})
            else:
                return render(request, 'regmsg.html', {'regester_data': register_data})
    else:
        user = UserForm()
    return render(request, 'register.html', {'user': user})


def authenticate(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=username, password=password)
    if not user:
        return redirect('login')
    auth.login(request, user)
    return redirect('index')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


def newform(request):
    if request.method == 'POST':
        contents = request.POST.get("text")
        if contents != "":
            times = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            information = Post(author=request.user, content=contents, created_at=times)
            information.save()
        return redirect('index')
    else:
        return render(request, 'index.html', {'user': user})


def changelikes(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            msg = request.POST.get("likes")
            if msg:
                name = request.user.id
                post_id = Record.objects.filter(name=name, post_id=msg, is_like=False)
                if len(post_id) != 0:
                    return redirect('index')
                message = Post.objects.get(id=msg)
                message.thumbs_up += 1
                inf = Record(name=request.user, post_id=msg, is_like=False)
                inf.save()
                message.save()
        
            dismsg = request.POST.get("dislikes")
            if dismsg:
                name = request.user.id
                post_id = Record.objects.filter(name=name, post_id=dismsg, is_like=True)
                if len(post_id) != 0:
                    return redirect('index')
                message = Post.objects.get(id=dismsg)
                message.thumbs_down += 1
                inf = Record(name=request.user, post_id=dismsg, is_like=True)
                inf.save()
                message.save()
            return redirect('index')
        else:
            return redirect('index')

