from django import forms

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from project1.models import TestModel,ModelEgor
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base

from .forms import UserForm
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']



@csrf_exempt
def reg(request):
    anna = TestModel()
    if request.method == 'POST':
        data = TestModel.objects.all()
        for i in data:
            if request.POST['email'] == i.email: return render(request, 'anna.html', {"err": "Данный Email занят"})
        if len(request.POST['password']) < 6: return render(request, 'anna.html', {"err": "Пароль слишком короткий"})
        anna.pole = 'Hello world'
        anna.email = request.POST['email']
        anna.password = request.POST['password']
        anna.save()
        return HttpResponse('Email'+' '+anna.email+' '+"успешно зарегистрирован!")

    return render(request, 'anna.html', {"err": ""})

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print('IMAGE UPLOAD')
        img = ImageForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            img_obj = img.instance
            return render(request, 'index.html', {'form': img, 'img_obj': img_obj})
    else:
        img = ImageForm()
    return render(request, 'index.html', {'form': img, 'img_obj': 'null'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # engine = create_engine('sqlite:///db.sqlite3')
        # Base = declarative_base()
        # Session = sessionmaker(bind=engine)
        # session = Session()
        # session.execute(text("""select * from project_modelanna"""))
        # data = session.flush()
        # session.close()
        data = TestModel.objects.all()
        for i in data:
            if email == i.email:
                if password == i.password:
                    return HttpResponse("Вы успешно прошли авторизацию!")
                else:
                    return HttpResponse("Пароль неверный")
        return HttpResponse("Такого пользователя не существует")
    return render(request, 'login.html')


@csrf_exempt
def danger(request):
    if request.method == 'POST':
        egor = ModelEgor()
        egor.password = '12456y'
        egor.name = request.POST['name']
        egor.save()
        print(f'{request.POST["name"]} запись сохранена!')
        print("MAIL: "+egor.email)
    return render(request, 'danger.html')





def profile(request):
    return None