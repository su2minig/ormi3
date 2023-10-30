from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, nickname, email, password):        
        if not email:            
            raise ValueError('must have user email')
        if not username:            
            raise ValueError('must have user id')
        if not password:            
            raise ValueError('must have user password')

        user = self.model(            
            email=email,
            username=username,
            nickname=nickname,       
        )        
        user.set_password(password)        
        user.save()        
        return user

    def create_superuser(self, username, nickname, email, password):        
    
        user = self.create_user(            
            email = email,
            username = username,
            nickname = nickname,               
            password=password,
            )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user 



class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
        )
    username = models.CharField(max_length=20, default="", unique=True)
    nickname = models.CharField(max_length=20, default="", unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email','nickname']

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    @property
    def is_staff(self):
        return self.is_admin
    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True