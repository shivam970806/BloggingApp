from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    user_pk = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='app1/static/images', default="")
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1500)
    heading = models.CharField(max_length=500, default="")
    #predefined to create table for same name
    class meta:
        db_table = "Blog"


class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    class meta:
        db_table = "Register"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=10)
    class meta:
        db_table = "Contact"

