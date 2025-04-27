from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser 

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
            return self.get(email=email)
    
    def create_user(self, email, password, first_name, last_name,  **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password, first_name, last_name,  **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        user = self.create_user(email, password, first_name, last_name, **extra_fields)
        return user


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255, blank=True, null = True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email
