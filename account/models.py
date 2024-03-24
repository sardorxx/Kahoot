import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    OPTION1 = 'Student'
    OPTION2 = 'Teacher'
    OPTION3 = 'Admin'

    CHOICES = [
        (OPTION1, 'Student'),
        (OPTION2, 'Teacher'),
        (OPTION3, 'Admin'),
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='users_image/')
    user_type = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=OPTION1,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # Add your additional fields here

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'user_type']

    def __str__(self):
        return self.username


class TeacherSettings(models.Model):
    teacher_settings_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    join_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.teacher_settings_id
