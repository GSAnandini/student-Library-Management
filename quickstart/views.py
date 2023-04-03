from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse

@api_view(['POST'])
def registerlibrary(request):
    serializer = LibrarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_lists(request):
    book_obj = Books.objects.all()
    serializer = BooksSerializer(book_obj, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        return Response({'error': 'Invalid Credentials'})
    if not user.check_password(password):
        return Response({'error': 'Invalid Credentials'})
    refresh = RefreshToken.for_user(user)
    response = redirect(reverse('registerlibrary'))
    response.set_cookie(key='access_token', value=str(refresh.access_token))
    return response


@api_view(['POST'])
def update_library(request,id):
    library_obj=Library.objects.get(id=id)
    serializer=LibrarySerializer(instance=library_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Data is updated!! ")
