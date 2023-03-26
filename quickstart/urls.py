from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('', home),
    path('books/', book_lists),
    path('library/', library_lists),
    path('register/', post_student),
    path('update/<int:id>/', update_student),
    path('updatelib/<int:id>/', update_library),
    path('delete/<int:id>/', delete_student),
]
