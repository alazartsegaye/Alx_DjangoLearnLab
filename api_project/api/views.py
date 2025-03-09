from django.shortcuts import render
from .models import Book
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .serializers import BookSerializer
import rest_framework.generics as generics
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

