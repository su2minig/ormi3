from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = settings.LOGIN_URL
)

def login(request):
    pass

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

def logout(request):
    pass

logout =LogoutView.as_view(
    next_page = settings.LOGOUT_URL
    # return redirect('login')
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# def logincheck(request):
#     if request.user.is_authenticated:
#         return HttpResponse("로그인 됨!")
#     return HttpResponse("로그인안됨!")

# @login_required
def logincheck(request):
    print(request.user.is_authenticated)
    print(request.user)
    return render(request, 'accounts/logincheck.html')

def loginfbv(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("로그인 성공")
        else:
            return HttpResponse("로그인 실패")
    else:
        # 로그인 폼 보여주기
        pass
    return render(request, 'accounts/loginfbv.html')