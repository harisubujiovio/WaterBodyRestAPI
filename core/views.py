from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.serializers import UserUpdateSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from .models import User
# Create your views here.

class UserViewSet(ModelViewSet):
    http_method_names = ['get','patch','delete']
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

