from django.db import models


class Date(models.Model):
    date = models.DateField()


class Name(models.Model):
    owner_name = models.CharField(max_length=255)


class Username(models.Model):
    user_name = models.EmailField()
