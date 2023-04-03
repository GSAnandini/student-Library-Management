from django.urls import path
from . import views
from .views import registerlibrary

urlpatterns = [
 
    path('books/', views.book_lists, name='book_lists'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('registerlibrary/', registerlibrary, name='registerlibrary'),
    path('updatelib/<int:id>/', views.update_library,name='update_library'),
]
