from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserForm

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

signup = CreateView.as_view(
    form_class = UserForm,
    template_name = 'accounts/form.html',
    success_url = '/accounts/login/'
)
