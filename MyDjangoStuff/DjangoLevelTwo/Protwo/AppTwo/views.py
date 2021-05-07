from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users

# Create your views here.


def help(request):
    userList = Users.objects.all()
    user_dict = {'user_list': userList}
    return render(request, "appTwo/help.html", context=user_dict)
