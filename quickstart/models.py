from django.db import models



class Books(models.Model):
    bookname = models.CharField(max_length=50,default='')
    author = models.CharField(max_length=50,default='') 


class Library(models.Model):
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=50,default='')
    books_issued_date = models.CharField(max_length=50,default='')
    id_no = models.CharField(max_length=50,default='')
    book_name = models.CharField(max_length=50,default='')
    author = models.CharField(max_length=50,default='')
    return_date = models.CharField(max_length=50,default='')
    book_status = models.CharField(max_length=50,default='')
