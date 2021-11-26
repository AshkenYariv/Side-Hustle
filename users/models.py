from django.db import models
from django.conf import settings
from django.contrib.auth.models import User as DjangoUser


# Enums
class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    UNSPECIFIED = 'U', 'Unspecified'


class Role(models.TextChoices):
    HR = 'hr', 'HR'
    STUDENT = 'student', 'Student'


# Model Classes:
class User(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.UNSPECIFIED,
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
        blank=True,
        null=True
    )
    password = models.CharField(max_length=100)

    @staticmethod
    def create_user(username, email, password, first_name, last_name, role, gender):
        django_user = DjangoUser.objects.create_user(username=username,
                                                     email=email,
                                                     password=password,
                                                     first_name=first_name,
                                                     last_name=last_name)
        user = User(user=django_user,
                    role=role,
                    gender=gender)
        user.save()
        return user

    def __str__(self) -> str:
        return self.first_name
