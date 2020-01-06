from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from application.models import Question
from adminboard.models import CreateCandidate
from django.http import HttpResponse
from django.contrib.auth.models import User
from application.models import Instructions
from django.core.cache import cache


def applogin(request):
    cache.clear()
    return render(request, 'application/index.html')

@csrf_exempt
def logincand(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('application:instructions')
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('application:applogin')
    return redirect('application:applogin')

@login_required(login_url='logincand/')
@csrf_exempt
def instructions(request):
    email = request.user.email
    username = request.user.username
    obj = CreateCandidate.objects.get(username=username)
    instruct = Instructions.objects.all().order_by('id')
    return render(request, 'application/instructions.html', {'username': username, 'name': obj.fullname, 'email': email, 'phone': obj.phone, 'instruct': instruct})

@login_required(login_url='logincand/')
def logout_user(request):
    logout(request)
    return redirect('application:applogin')

@login_required(login_url='logincand/')
def panel(request):
    username = request.user.username
    english_questions = Question.objects.filter(category__iexact='english').order_by('?')[:10]
    quantitative_questions = Question.objects.filter(category__iexact='quantitative').order_by('?')[:10]
    reasoning_questions = Question.objects.filter(category__iexact='reasoning').order_by('?')[:30]
    return render(request, 'application/panel.html', {'english_questions': english_questions, 'quantitative_questions': quantitative_questions,
                                                      'reasoning_questions': reasoning_questions, 'username': username})

@login_required(login_url='logincand/')
@csrf_exempt
def submitted(request):
    if request.method == 'POST':
        percent = request.POST.get('percent__')
        username = request.POST.get('username__')
        try:
            user = CreateCandidate.objects.get(username=username)
            user.score = percent
            user.teststatus = 'Test Taken'
            user.status = 'Test Taken'
            user.save()
        except:
            return HttpResponse('<h2>Unique contraint failed for username</h2>')
        logout(request)
        return render(request, 'application/submit.html')
    return redirect('application:panel')


def forcelogout(request, username):
    User.objects.get(username=username).delete()
    logout(request)
    return redirect('application:applogin')
