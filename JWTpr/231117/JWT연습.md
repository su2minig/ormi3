python -m venv venv # 가상환경 생성

.\venv\Scripts\activate # window

pip install django # django 설치

django-admin startproject project . # project 프로젝트 생성

python manage.py startapp accounts # accounts 앱 생성

settings.py > INSTALLED_APPS에 새로 생성한 앱 추가

# Custom User 모델 구현

### custom user 모델을 아래와 같이 구현해주세요.

1. username 필드는 사용하지않습니다.
2. 로그인시 email 필드를 사용합니다.
3. gender 필드를 추가하여 여자/남자 중에 선택할 수 있도록 해주세요.
4. date_of_birth 필드를 추가해주세요.

# accounts > managers.py 생성
```python
# accounts/managers.py
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
```

# accounts > models.py

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

GENDER_CHOICES = (
    ('male', '남자'),
    ('female', '여자'),
)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email
```

# settings.py 밑에 AUTH_USER_MODLE을 추가하여 만든 User모델을 사용하기위해 선언합니다.

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

# 모델 변경사항 DB에 적용
```python
python manage.py makemigrations
python manage.py migrate
```

# 커스텀한 유저 모델 어드민 페이지에서 관리하기위해 등록

```python
from django.contrib import admin
from accounts.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
```

# requirements.txt에 있는 라이브러리 설치
```
pip install -r requirments.txt
```

# 설치한 라이브러리 사용을 위해 settings.py에 추가
```python
INSTALLED_APPS = [
...
    # 설치한 라이브러리들
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
...
]

from datetime import timedelta

... 생략 ...

# dj-rest-auth
REST_USE_JWT = True # JWT 사용 여부
JWT_AUTH_COOKIE = 'my-app-auth' # 호출할 Cookie Key 값
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' # Refresh Token Cookie Key 값

# django-allauth
SITE_ID = 1 # 해당 도메인 id
ACCOUNT_UNIQUE_EMAIL = True # User email unique 사용 여부
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # 사용자 이름 필드 지정
ACCOUNT_USERNAME_REQUIRED = False # User username 필수 여부
ACCOUNT_EMAIL_REQUIRED = True # User email 필수 여부
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 로그인 인증 수단
ACCOUNT_EMAIL_VERIFICATION = 'none' # email 인증 필수 여부

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # AccessToken 유효 기간 설정
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # RefreshToken 유효 기간 설정
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

# python manage.py migrate

# 회원가입 처리할 url설정
```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls"))
]
```
```python
# accounts/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('join/', include("dj_rest_auth.registration.urls")),
]
```

# 로그인 처리를 위한 url설정
```python
# accounts/urls.py
from django.urls import path, include

urlpatterns = [
...
    path("", include("dj_rest_auth.urls")),
...
]
```

# 런서버
```python
# No module named 'pkg_resources'에러가 나면 아래 코드를 실행해주세요.
pip install --upgrade setuptools
# pip install --upgrade distribute # 위에것만 해도 되실텐데 안되시면 아래 명령어도 입력해주세요.
```

# 
```python
# accounts/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import example_view

urlpatterns = [
    path('test/', example_view),
    path('join/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
    path('mypage/', views.getmypage, name='mypage'),
]
```

```python
# accounts/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request):
    # request.user는 인증된 사용자의 정보를 담고 있습니다.
    print(request.data)
    content = {'message': 'Hello, World!', 'user': str(request.user)}
    return Response(content)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getmypage(request):
    print(request.data)
    print(request.headers)
    content = {'message': '반갑습니다', 'user': str(request.user)}
    return Response(content)
```
