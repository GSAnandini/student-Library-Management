from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


# READ operation
@api_view(['GET'])
def home(request):
    student_obj=Student.objects.all()
    serializer=StudentSerializer(student_obj,many=True)
    return Response(serializer.data)

# READ operation for books
@api_view(['GET'])
def book_lists(request):
    book_obj = Books.objects.all()
    serializer = BooksSerializer(book_obj, many=True)
    return Response(serializer.data)

# READ operation for library
@api_view(['GET'])
def library_lists(request):
    library_obj = Library.objects.all()
    serializer = LibrarySerializer(library_obj, many=True)
    return Response(serializer.data)

# CREATE operation
@api_view(['POST'])
def post_student(request):
    student_obj = Student.objects.filter(name=request.data['name'], email=request.data['email'],password=request.data['password'] )
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        if student_obj.exists():
            return Response("You are already a registered user!! ", status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response("Your registration is successfull !! ", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UPDATE operation
@api_view(['POST'])
def update_student(request,id):
    student_obj=Student.objects.get(id=id)
    serializer=StudentSerializer(instance=student_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# UPDATE operation for library
@api_view(['POST'])
def update_library(request,id):
    library_obj=Library.objects.get(id=id)
    serializer=LibrarySerializer(instance=library_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Data is updated!! ")

# DELETE operation
@api_view(['DELETE'])
def delete_student(request,id):
    student_obj=Student.objects.get(id=id)
    student_obj.delete()
    return Response("Student is deleted! ")
