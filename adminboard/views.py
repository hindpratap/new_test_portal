from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from adminboard.models import Authorizedadmin, CreateCandidate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from application.models import Question
from adminboard.tasks import sendmailtask
from django.db.models import Q
import pandas as pd
import numpy as np


def adminlogin(request):
    return render(request, 'adminboard/login.html')

@login_required
def adminhome(request):
    obj = Authorizedadmin.objects.all()
    authorized_admin = [i.email for i in obj]
    email = request.user.email
    candidate_cont = CreateCandidate.objects.all().count()
    candidate_under_review = CreateCandidate.objects.exclude(Q(selectionstatus__iexact='selected') | Q(selectionstatus__iexact='rejected')).count()
    candidate_selected = CreateCandidate.objects.filter(selectionstatus__iexact='selected').order_by('-id')
    return render(request, 'adminboard/home.html', {'authorized_admin': authorized_admin, 'email': email, 'candidate_count': candidate_cont,
                                                    'candidate_under_review': candidate_under_review, 'candidate_selected':candidate_selected})

@login_required
def logoutAdmin(request):
    logout(request)
    return redirect('adminboard:adminlogin')

@login_required
def adminuser(request):
    global authorized_admin
    obj = Authorizedadmin.objects.all()
    email = request.user.email
    authorized_admin = [i.email for i in obj]
    candidates = CreateCandidate.objects.filter(activestatus__iexact='active').order_by('-id')
    return render(request, 'adminboard/user.html', {'authorized_admin': authorized_admin, 'email':email, 'candidates':candidates})

@login_required
def addcredential(request):
    obj = Authorizedadmin.objects.all()
    authorized_admin = [i.email for i in obj]
    email = request.user.email
    data = CreateCandidate.objects.all()
    return render(request, 'adminboard/cred.html', {'authorized_admin': authorized_admin, 'email':email, 'data':data})

@login_required
@csrf_exempt
def postcred(request):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if request.method == 'POST' and email in authorized_admin:
        fullname = request.POST.get('fullName')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        designation = request.POST.get('profile')
        team = request.POST.get('team')
        dob = request.POST.get('dob')
        resume = request.FILES.get('resume')

        dob = dob[6:10] + '-' + dob[:2] + '-' + dob[3:5]
        if User.objects.filter(username=username).exists() and CreateCandidate.objects.filter(username=username).exists():
            try:
                authcand = User.objects.get(username=username)
                cand = CreateCandidate.objects.get(username=username)
                authcand.first_name = fullname
                authcand.email = email
                authcand.save()
                cand.fullname = fullname
                cand.email = email
                cand.phone = phone
                cand.team = team
                cand.designation = designation
                if resume != None:
                    cand.resume = resume
                else:
                    pass
                cand.save()
            except:
                return HttpResponse('<h2>Error code v6s v7.5s(postcred if)</h2>')
            return redirect('adminboard:adminuser')
        else:
            try:
                CreateCandidate.objects.create(fullname=fullname, username=username, password=password, email=email,
                                            phone=phone, designation=designation, team=team, created_at=datetime.today(), dob=dob, resume=resume)
                User.objects.create_user(first_name=fullname, username=username, password=password, email=email)

            except:
                return HttpResponse('<h2>Error code v8-8.5s(postcred else)</h2>')
            return redirect('adminboard:addcredential')
    return redirect('adminboard:addcredential')

@login_required
def admineditcand(request, username):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    try:
        email = request.user.email
        obj = CreateCandidate.objects.get(username=username)
        return render(request, 'adminboard/editcred.html', {'candidate': obj, 'email': email, 'authorized_admin': authorized_admin})
    except:
        return HttpResponse('<h2>Error: V@admineditcand</h2>')

@login_required
def admindelcand(request, username):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if email in authorized_admin:
        try:
            User.objects.get(username=username).delete()
            obj = CreateCandidate.objects.get(username=username)
            obj.activestatus = 'deleted'
            obj.save()
            return redirect('adminboard:adminuser')
        except:
            return HttpResponse('<h2>Error: V@admindelcand</h2>')
    else:
        return HttpResponse('<h2>Error: You do not have admin rights.</h2>')

def adminnotifycand(request, username):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if email in authorized_admin:
        sub = 'test sub'
        mail = username
        # sendmailtask.delay(sub, mail)
        user = CreateCandidate.objects.get(username=username)
        user.invitestatus = 'Invite sent'
        user.save()
        return redirect('adminboard:adminuser')
    else:
        return HttpResponse('<h2>Error: You do not have admin rights.</h2>')

@login_required
@csrf_exempt
def addquest(request):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if email in authorized_admin:
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('opt1')
            option2 = request.POST.get('opt2')
            option3 = request.POST.get('opt3')
            option4 = request.POST.get('opt4')
            option5 = request.POST.get('opt5')
            correct = request.POST.get('correct')
            category = request.POST.get('category')
            if option5 == '':
                Question.objects.create(question=question, option1=option1, option2=option2,
                                        option3=option3, option4=option4, correct=correct,
                                        category=category)
            else:
                Question.objects.create(question=question, option1=option1, option2=option2,
                                        option3=option3, option4=option4, correct=correct, option5=option5,
                                        category=category)
            return render(request, 'adminboard/quest.html')

        return render(request, 'adminboard/quest.html')
    else:
        return HttpResponse('<h2>Error: You do not have admin rights.</h2>')

@login_required
def viewquest(request):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    questions = Question.objects.all().order_by('-id')
    return render(request, 'adminboard/viewQuest.html', {'questions': questions, 'email': email, 'authorized_admin': authorized_admin})

@login_required
def delquest(request, quest):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if email in authorized_admin:
        Question.objects.get(pk=quest).delete()
        return redirect('adminboard:viewquest')
    else:
        return HttpResponse('<h2>Error: You do not have admin rights.</h2>')

@login_required
def editquest(request, quest):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    question = Question.objects.get(pk=quest)
    return render(request, 'adminboard/editquest.html', {'question': question, 'email': email, 'authorized_admin': authorized_admin})

@login_required
def submission(request):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    data = CreateCandidate.objects.filter(teststatus__iexact='TestTaken')
    return render(request, 'adminboard/submission.html', {'data': data, 'email': email, 'authorized_admin': authorized_admin})

@login_required
def changequest(request):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if email in authorized_admin:
        try:
            if request.method == 'POST':
                question = request.POST.get('question')
                option1 = request.POST.get('opt1')
                option2 = request.POST.get('opt2')
                option3 = request.POST.get('opt3')
                option4 = request.POST.get('opt4')
                option5 = request.POST.get('opt5')
                correct = request.POST.get('correct')
                category = request.POST.get('category')
                questid = request.POST.get('questid')
                obj = Question.objects.get(pk=questid)
                obj.question = question
                obj.option1 = option1
                obj.option2 = option2
                obj.option3 = option3
                obj.option4 = option4
                obj.option5 = option5
                obj.correct = correct
                obj.category = category
                obj.save()
                return redirect('adminboard:viewquest')
            return redirect('adminboard:viewquest')
        except:
            return HttpResponse('<h2>Error: V@changequest</h2>')
    else:
        return HttpResponse('<h2>You do not have admin rights.</h2>')


@login_required
@csrf_exempt
def candaction(request, id):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if email in authorized_admin:
        try:
            obj = CreateCandidate.objects.get(pk=id)
            if 'accept' in request.POST:
                obj.selectionstatus = 'Selected'
                obj.save()
            elif 'reject' in request.POST:
                obj.selectionstatus = 'Rejected'
                obj.save()
            return redirect('adminboard:submission')
        except:
            return HttpResponse('<h2>Error: V@candaccept</h2>')
    else:
        return HttpResponse('<h2>You do not have admin rights.</h2>')

@login_required
@csrf_exempt
def bulkupload(request):
    authorized_admin = [i.email for i in Authorizedadmin.objects.all()]
    email = request.user.email
    if email in authorized_admin:
        if request.method == 'POST':
            try:
                csvfile = request.FILES.get('bulk')
                df_quest = pd.read_csv(csvfile)
                df_quest = df_quest.replace(np.nan, 'null')

                def appendquest(x):
                    if x['Comprehension'] == 'null':
                        return x['Question']
                    else:
                        question = x['Comprehension'] + '\n' + x['Question']
                        return question

                df_quest['question'] = df_quest.apply(appendquest, axis=1)
                df_quest.drop(['Comprehension', 'Question'], axis=1, inplace=True)

                def categorize(x):
                    if 'reasoning' in str.lower(x['Category']) and 'quantitative' not in str.lower(x['Category']):
                        return 'Reasoning'
                    elif 'reasoning' in str.lower(x['Category']) and 'quantitative' in str.lower(x['Category']):
                        return 'Quantitative'
                    elif 'quantitative' in str.lower(x['Category']):
                        return 'Quantitative'
                    elif 'sentence' in str.lower(x['Category']) and 'correction' in str.lower(x['Category']):
                        return 'English'
                    elif 'reading' in str.lower(x['Category']) and 'comprehension' in str.lower(x['Category']):
                        return 'English'
                    else:
                        return 'Not detected'

                df_quest['category_proper'] = df_quest.apply(categorize, axis=1)

                df_quest = df_quest[['question', 'Option A', 'Option B', 'Option C', 'Option D', 'Option E',
                                     'Answer', 'category_proper']]
                df_quest.columns = ['question', 'option1', 'option2', 'option3', 'option4', 'option5',
                                    'correct', 'category']
                for i in range(len(df_quest)):
                    Question.objects.create(question=df_quest.iloc[i, 0], option1=df_quest.iloc[i, 1], option2=df_quest.iloc[i, 2],
                                            option3=df_quest.iloc[i, 3], option4=df_quest.iloc[i, 4], option5=df_quest.iloc[i, 5],
                                            correct=df_quest.iloc[i, 6], category=df_quest.iloc[i, 7])

                return redirect('adminboard:viewquest')
            except:
                return HttpResponse('<h2>Error: Incorrect file format</h2>')
        return redirect('adminboard:addquest')
    else:
        return HttpResponse('You do not have admin rights.')