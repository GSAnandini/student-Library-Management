from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='default_password')


class Books(models.Model):
    bookname = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

class Library(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    books_issued_date = models.CharField(max_length=50)
    id_no = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    return_date = models.CharField(max_length=50)
    book_status = models.CharField(max_length=50)
# Create your models here.

