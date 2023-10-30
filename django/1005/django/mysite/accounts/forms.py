from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'password1', 'password2',]