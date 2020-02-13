from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from adminboard.models import AuthorizedHr, CreateCandidate, History
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from application.models import Question
from adminboard.tasks import sendmailtask
import pandas as pd
import numpy as np
from application.models import Instructions
from django.core.cache import cache
from itertools import chain
from django.core.mail import send_mail
from django.conf import settings


def adminlogin(request):
    cache.clear()
    return render(request, 'adminboard/login.html')

def adminhome(request):
    if request.user.is_authenticated:
        obj = AuthorizedHr.objects.all()
        authorized_admin = [i.email for i in obj]
        email = request.user.email
        candidate_cont = CreateCandidate.objects.all().count()
        pending_submissions = CreateCandidate.objects.filter(invitestatus__iexact='Invite sent', teststatus__iexact='Pending')
        pending_submissions_count = pending_submissions.count()
        candidate_shortlisted = CreateCandidate.objects.filter(score__gte=70)
        candidate_shortlisted_count = candidate_shortlisted.count()
        return render(request, 'adminboard/home.html', {'authorized_admin': authorized_admin, 'email': email, 'candidate_count': candidate_cont,
                                                        'pending_submissions': pending_submissions, 'candidate_shortlisted':candidate_shortlisted,
                                                        'candidate_shortlisted_count': candidate_shortlisted_count,
                                                        'pending_submissions_count': pending_submissions_count})
    else:
        return redirect('adminboard:adminlogin')


def logoutAdmin(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('adminboard:adminlogin')
    else:
        return redirect('adminboard:adminlogin')

def adminuser(request):
    if request.user.is_authenticated:
        global authorized_admin
        obj = AuthorizedHr.objects.all()
        email = request.user.email
        authorized_admin = [i.email for i in obj]
        candidates = CreateCandidate.objects.all().order_by('-id')
        return render(request, 'adminboard/user.html', {'authorized_admin': authorized_admin, 'email': email, 'candidates': candidates})
    else:
        return redirect('adminboard:adminlogin')

def addcredential(request):
    if request.user.is_authenticated:
        obj = AuthorizedHr.objects.all()
        authorized_admin = [i.email for i in obj]
        email = request.user.email
        data1 = CreateCandidate.objects.all()
        data2 = User.objects.all()
        data = list(chain(data1, data2))
        return render(request, 'adminboard/cred.html', {'authorized_admin': authorized_admin, 'email':email, 'data':data})
    else:
        return redirect('adminboard:adminlogin')

@csrf_exempt
def postcred(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        filler_email = request.user.email
        if request.method == 'POST' and filler_email in authorized_admin:
            fullname = request.POST.get('fullName')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            designation = request.POST.get('profile')
            team = request.POST.get('team')
            dob = request.POST.get('dob')
            resume = request.FILES.get('resume')
            location = request.POST.get('location')
            source = request.POST.get('source')
            referral = request.POST.get('referral')
            dob = dob[6:10] + '-' + dob[:2] + '-' + dob[3:5]
            if User.objects.filter(username=username).exists() and CreateCandidate.objects.filter(username=username).exists():
                # try:
                authcand = User.objects.get(username=username)
                authcand.first_name = fullname
                authcand.email = email
                authcand.save()
                cand = CreateCandidate.objects.get(username=username)
                cand.fullname = fullname
                cand.email = email
                cand.phone = phone
                cand.team = team
                cand.designation = designation
                cand.location = location
                cand.source = source
                cand.referralid = referral
                cand.dob = dob
                # cand.dob = dob
                if resume != None:
                    cand.resume = resume
                else:
                    pass
                cand.save()
                History.objects.create(fullname=fullname, username=username, password=password, email=email,
                                               phone=phone, designation=designation, team=team, created_at=datetime.today(),
                                               dob=dob, resume=resume, location=location, source=source,
                                               referralid=referral, updated_at=datetime.now(), updated_by=filler_email)

                # except:
                #     return HttpResponse('<h2>Error code v6s v7.5s(postcred if)</h2>')
                return redirect('adminboard:adminuser')
            else:
                # try:
                CreateCandidate.objects.create(fullname=fullname, username=username, password=password, email=email,
                                            phone=phone, designation=designation, team=team, created_at=datetime.today(), dob=dob, resume=resume, location=location, source=source, referralid=referral)
                History.objects.create(fullname=fullname, username=username, password=password, email=email,
                                               phone=phone, designation=designation, team=team, created_at=datetime.today(),
                                               dob=dob, resume=resume, location=location, source=source,
                                               referralid=referral, updated_at=datetime.now(), updated_by=filler_email)
                User.objects.create_user(first_name=fullname, username=username, password=password, email=email)

                # except:
                #     return HttpResponse('<h2>Error code v8-8.5s(postcred else)</h2>')
                return redirect('adminboard:addcredential')
        return redirect('adminboard:addcredential')
    else:
        return redirect('adminboard:adminlogin')


def admineditcand(request, username):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        try:
            email = request.user.email
            obj = CreateCandidate.objects.get(username=username)
            return render(request, 'adminboard/editcred.html', {'candidate': obj, 'email': email, 'authorized_admin': authorized_admin})
        except:
            return HttpResponse('<h2>Error: V@admineditcand</h2>')
    else:
        return redirect('adminboard:adminlogin')


def admindelcand(request, username):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        if email in authorized_admin:
            # try:
            User.objects.get(username=username).delete()
            obj = CreateCandidate.objects.get(username=username)
            obj.activestatus = 'deleted'
            obj.save()
            return redirect('adminboard:adminuser')
            # except:
            #     return HttpResponse('<h2>Error: V@admindelcand</h2>')
        else:
            return HttpResponse('<h2>Error: You do not have admin rights.</h2>')
    else:
        return redirect('adminboard:adminlogin')

def adminnotifycand(request, username):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        filler_email = request.user.email
        if filler_email in authorized_admin:
            recreate_cand = CreateCandidate.objects.get(username=username)
            if User.objects.filter(username=username).exists():
                pass
            else:
                User.objects.create_user(username=username, password=recreate_cand.password, first_name=recreate_cand.fullname, email=recreate_cand.email)
            sub = 'no-reply: Test details'
            content = f'Hi {recreate_cand.fullname},\nThank you for showing interest in working with DataFlow Group.\nTo complete the application process, you are required to take an online test. The test would include assessment for English Grammar, Logic Check and Reasoning Skills.\n\nBelow are the credentials for the test:\n\nusername- {recreate_cand.username}\npassword- {recreate_cand.password}\nTest link: https://uataudit.dfgateway.com\nThe test cannot be fragmented, but must be completed in a single attempt. The duration for the test is 30 minutes.\n\nBest Regards\nHR Team- Dataflow Group'
            tomail = [f'{recreate_cand.email}']
            # sendmailtask.delay(sub, content, tomail)
            send_mail(sub, content, settings.EMAIL_HOST_USER, tomail)
            user = CreateCandidate.objects.get(username=username)
            user.invitestatus = 'Invite sent'
            user.status = 'Invite sent'
            user.save()
            History.objects.create(username=user.username, password=user.password,
                                   phone=user.phone, fullname=user.fullname, designation=user.designation,
                                   email=user.email, team=user.team, location=user.location, score=user.score,
                                   invitestatus='Invite Sent', teststatus=user.teststatus,
                                   status='Invite Sent', selectionstatus=user.selectionstatus,dob=user.dob, resume=user.resume, created_at=user.created_at,
                                   activestatus=user.activestatus, source=user.source, referralid=user.referralid,
                                   candempid=user.candempid, updated_at=datetime.now(), updated_by=filler_email)
            return redirect('adminboard:adminuser')
        else:
            return HttpResponse('<h2>Error: You do not have admin rights.</h2>')
    else:
        return redirect('adminboard:adminlogin')

@csrf_exempt
def addquest(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
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
    else:
        return redirect('adminboard:adminlogin')

def viewquest(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        questions = Question.objects.all().order_by('-id')
        return render(request, 'adminboard/viewQuest.html', {'questions': questions, 'email': email, 'authorized_admin': authorized_admin})
    else:
        return redirect('adminboard:adminlogin')


def delquest(request, quest):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        if email in authorized_admin:
            Question.objects.get(pk=quest).delete()
            return redirect('adminboard:viewquest')
        else:
            return HttpResponse('<h2>Error: You do not have admin rights.</h2>')
    else:
        return redirect('adminboard:adminlogin')

def editquest(request, quest):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        question = Question.objects.get(pk=quest)
        return render(request, 'adminboard/editquest.html', {'question': question, 'email': email, 'authorized_admin': authorized_admin})
    else:
        return redirect('adminboard:adminlogin')


def submission(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        data = CreateCandidate.objects.filter(teststatus__iexact='test taken').order_by('-id')
        return render(request, 'adminboard/submission.html', {'data': data, 'email': email, 'authorized_admin': authorized_admin})
    else:
        return redirect('adminboard:adminlogin')


def changequest(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
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
    else:
        return redirect('adminboard:adminlogin')


@csrf_exempt
def candaction(request, id):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        filler_email = request.user.email
        if request.method == 'POST' and filler_email in authorized_admin:
            fStatus = request.POST.get('fStatus')
            empId = request.POST.get('empId')
            try:
                user = CreateCandidate.objects.get(pk=id)
                user.selectionstatus = fStatus
                user.candempid = empId
                user.save()

                History.objects.create(username=user.username, password=user.password,
                                                  phone=user.phone, fullname=user.fullname, designation=user.designation,
                                                  email=user.email, team=user.team, location=user.location, score=user.score,
                                                  invitestatus=user.invitestatus, teststatus='Test Taken',
                                                  status=fStatus, dob=user.dob, resume=user.resume, created_at=user.created_at,
                                                  activestatus=user.activestatus, selectionstatus=fStatus, source=user.source, referralid=user.referralid,
                                                  candempid=empId, updated_at=datetime.now(), updated_by=filler_email)
                return redirect('adminboard:submission')
            except:
                return HttpResponse('<h2>Error: V@candaccept</h2>')
        else:
            return HttpResponse('<h2>You do not have admin rights.</h2>')
    else:
        return redirect('adminboard:adminlogin')


@csrf_exempt
def bulkupload(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        filler_email = request.user.email
        if filler_email in authorized_admin:
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
    else:
        return redirect('adminboard:adminlogin')


def other(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        instruct = Instructions.objects.all().order_by('-id')
        return render(request, 'adminboard/other.html', {'email': email, 'authorized_admin': authorized_admin, 'instruct': instruct})
    else:
        return redirect('adminboard:adminlogin')


def delinstructions(request, inst):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        if email in authorized_admin:
            Instructions.objects.get(pk=inst).delete()
            return redirect('adminboard:other')
        else:
            return HttpResponse('<h2>Error: You do not have admin rights.</h2>')
    else:
        return redirect('adminboard:adminlogin')

@csrf_exempt
def postinstructions(request):
    if request.user.is_authenticated:
        authorized_admin = [i.email for i in AuthorizedHr.objects.all()]
        email = request.user.email
        if request.method == 'POST' and email in authorized_admin:
            instr = request.POST.get('instruction')
            Instructions.objects.create(points=instr)
            return redirect('adminboard:other')
        return redirect('adminboard:other')
    else:
        return redirect('adminboard:adminlogin')

