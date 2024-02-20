from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo


# Create your views here.

def user_list(request):
    user_data = UserInfo.objects.all()

    return render(request, "user_list.html", {'user_data': user_data})


def user_add(request):
    if request.method == 'GET':
        return render(request, "user_add.html")

    user_name = request.POST.get('name')
    user_password = request.POST.get('password')
    user_age = request.POST.get('age')

    UserInfo.objects.create(name=user_name, password=user_password, age=user_age)
    return redirect('/user/list/')


def user_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
