from django.db import models
from django.contrib.auth.models import User
# from django.db.models import AutoField
# from django.db.models.BigAutoField import BigAutoField


# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,null =True,blank =True)
    enrolment = models.CharField(max_length =50)
    year_sem = models.CharField(max_length = 50)
    department = models.CharField(max_length=30)
    # email = models.EmailField(unique=True)
    # reg_number = models.OneToOneField()

class Category(models.Model):
    name = models.CharField("Category",max_length =50)
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.name
    

class Book(models.Model):
    book_name= models.CharField(max_length= 50)
    Author = models.CharField(max_length= 50)
    ISBN = models.PositiveIntegerField()
    summery = models.TextField()

    cover_image = models.ImageField(upload_to ="img",null = False, blank=False)
    category = models.ManyToManyField(Category, related_name="books")
    # pdf = models.FileField(upload_to='pdf',null =True,blank =True)
    recommended_books = models.BooleanField(default=False)
    coding_books= models.BooleanField(default =False)
    business_book = models.BooleanField(default =False)
    friction_books = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name


class Issuebook(models.Model):
    enrolment = models.CharField(max_length=50)
    ISBN = models.PositiveIntegerField(max_length=50)
    issu_date = models.DateField(auto_now=True)
    expary_date = models.DateField()
    