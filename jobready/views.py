from django.shortcuts import render, redirect

from .forms import *
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models


# Create your views here.
class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''

def index(request):
    return render(request, "index.html")


def fresherquestion(request):
    return render(request, "fresherQuestion.html")


def java(requset):
    questions = fresherQuestion.objects.all()
    return render(requset, "java.html", {'questions': questions})


def cProgram(requset):
    questions = fresherQuestion.objects.all()
    return render(requset, "c.html", {'questions': questions})


def php(requset):
    questions = fresherQuestion.objects.all()
#    if questions.Category == 'PHP':
    return render(requset, "php.html", {'questions': questions})


def about(request):
    return render(request, "about.html")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('Login')
        else:
            messages.info('password did not match')
            return redirect('Register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'invalid cred')
            return redirect('Login')
    else:
        return render(request, 'login.html')

def comreview(request):
    cReview = company_Reviews.objects.all()
    form = reviewForm()

    if request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/comReview')

        context = {'cReview': cReview, 'form': form}
    return render(request, 'company_review.html', context)


def logout(request):
    auth.logout(request)
    return redirect('Login')

def Google(requset):
    questions = company_Reviews.objects.all()
    return render(requset, 'review_google.html', {'questions': questions})

def Facebook(requset):
    questions = company_Reviews.objects.all()
    return render(requset, 'review_facebook.html', {'questions': questions})

def Khoros(requset):
    counter = Counter()
    counter.increment()
    questions = company_Reviews.objects.all()
    return render(requset, 'review_khoros.html', {'questions': questions})
