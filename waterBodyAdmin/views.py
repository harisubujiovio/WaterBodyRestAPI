from pickle import FALSE, TRUE
import os
from pprint import pprint
from sre_parse import FLAGS
from django.db import connection
from fastkml import kml
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination


from waterbody.settings import BASE_DIR
from .models import Role, SurveyQuestionMetaData, TankImage, TankMetaData, UserProfile
from .serializers import RoleSerializer, RoleUpdateSerializer, SurveyQuestionDataSerializer, TankImageSerializer, TankMetaDataSerializer, UserProfileAddSerializer, UserProfileSerializer, UserProfileUpdateSerializer
# Create your views here.



class RoleViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = Role.objects.prefetch_related('users').all()
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name', 'description' )
    ordering_fields = [ 'name', 'description' ]

    def get_serializer_class(self):
         if self.request.method == 'PATCH':
             return RoleUpdateSerializer
         return RoleSerializer

    def destroy(self, request, pk):
        role = get_object_or_404(Role,pk=pk)
        if role.users.count() > 0:
            return Response( { 'error': 'Role cannot be deleted because it is associated with users'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(ListAPIView, GenericViewSet):
     queryset = UserProfile.objects.select_related('user').select_related('role').all()
     serializer_class = UserProfileSerializer
     filter_backends = (SearchFilter, OrderingFilter)
     pagination_class = LimitOffsetPagination
     search_fields = ( 'user__first_name', 'user__last_name', 'user__email' )
     ordering_fields = [ 'user__first_name', 'user__last_name', 'user__email' ]


class UserProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = UserProfile.objects.select_related('user').all()

    def get_serializer_class(self):
         if self.request.method == 'POST':
             return UserProfileAddSerializer
         elif self.request.method == 'PATCH':
             return UserProfileUpdateSerializer
         else: 
            return UserProfileSerializer
              

    @action(detail=False, methods=['GET','PUT'])
    def me(self,request):
        (userProfile,created) = UserProfile.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = UserProfileSerializer(userProfile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserProfileSerializer(userProfile,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def deleteUser(self, request, *args, **kwargs):
        user_id = int(kwargs['user_id'])
        id = kwargs['pk']
        userprofile = UserProfile(pk=id)
        userprofile.delete()
        with connection.cursor() as cursor:
          cursor.execute("DELETE from core_user where id = %s", [user_id])
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PATCH'], detail=True)
    def updateUser(self, request, *args, **kwargs):
        user_id = int(kwargs['user_id'])
        id = kwargs['pk']
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        with connection.cursor() as cursor:
          cursor.execute("update core_user set first_name=%s,last_name=%s where id = %s", [first_name,last_name,user_id])
        userProfile = UserProfile.objects.get(id=id)
        serializer = UserProfileUpdateSerializer(userProfile,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TankMetaDataViewSet(ModelViewSet):
    serializer_class = TankMetaDataSerializer
    queryset = TankMetaData.objects.all()

    @action(detail=False, methods=['GET'],url_path=r'getTankMetaData/(?P<id>\d+)')
    def getTankMetaData(self, request, id):
        querySet = TankMetaData.objects.filter(tankId_id = id)
        serializer = TankMetaDataSerializer(querySet.first())
        return Response(serializer.data)

class SurevyQuestionViewSet(ModelViewSet):
    serializer_class = SurveyQuestionDataSerializer
    queryset = SurveyQuestionMetaData.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'question','statusText' )
    ordering_fields = [ 'question','statusText' ]


class TankImageViewSet(ModelViewSet):
    serializer_class = TankImageSerializer
    queryset = TankImage.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'image' )
    ordering_fields = [ 'image' ]
    

    @action(detail=False, methods=['GET'],url_path=r'ProcessTankMetaData/(?P<id>\d+)')
    def ProcessTankMetaData(self,request,id):
         (tank_image,created) = TankImage.objects.get_or_create(id=id)
         with open(tank_image.image.path, 'rt', encoding="utf-8") as myfile:
          doc=myfile.read()
          k = kml.KML()
          k.from_string(doc)
          features = list(k.features())
          y = len(features)
          f2 = list(features[0].features())
          z = len(f2)
          description = f2[0].description
          name = f2[0].name
          soup = BeautifulSoup(description)
          tables = soup.find_all('table')
          print(len(tables))
          cnt = 0
          datatable = tables[1]
          dicts = {}
          rows = datatable.find_all('tr', recursive=False)
          keyname = ''
          for row in rows:
             cells = row.find_all(['td'], recursive=False)
             for num, cell in enumerate(cells):
                 if num % 2 > 0:
                      dicts[keyname] = cell.text
                 else:
                      dicts[cell.text] = ''
                      keyname = cell.text

          
          if len(dicts) > 0:
              tankMetaData = TankMetaData()
              tankMetaData.tankId = tank_image
              tankMetaData.FID = dicts["FID"]
              tankMetaData.CLUSTER = dicts["CLUSTER"]
              tankMetaData.TANK_NUM = dicts["TANK_NUM"]
              tankMetaData.Unique_id = dicts["Unique_id"]
              tankMetaData.Tank_Name = dicts["Tank_Name"]
              tankMetaData.Latitude = dicts["Latitude"]
              tankMetaData.Longitude = dicts["Longitude"]
              tankMetaData.Village = dicts["Village"]
              tankMetaData.Block = dicts["Block"]
              tankMetaData.Taluk = dicts["Taluk"]
              tankMetaData.District = dicts["District"]
              tankMetaData.Subbasin = dicts["Subbasin"]
              tankMetaData.Basin = dicts["Basin"]
              tankMetaData.Section = dicts["Section"]
              tankMetaData.Sub_Dn = dicts["Sub_Dn"]
              tankMetaData.Division = dicts["Division"]
              tankMetaData.Circle = dicts["Circle"]
              tankMetaData.Region = dicts["Region"]
              tankMetaData.Tank_Type = dicts["Tank_Type"]
              tankMetaData.Cap_MCM = dicts["Cap_MCM"]
              tankMetaData.FTL_m = dicts["FTL_m"]
              tankMetaData.MWL_m = dicts["MWL_m"]
              tankMetaData.TBL_m = dicts["TBL_m"]
              tankMetaData.Sto_Dep_m = dicts["Sto_Dep_m"]
              tankMetaData.Ayacut_ha = dicts["Ayacut_ha"]
              tankMetaData.Catch_sqkm = dicts["Catch_sqkm"]
              tankMetaData.Wat_Spr_ha = dicts["Wat_Spr_ha"]
              tankMetaData.No_of_Weir = dicts["No_of_Weir"]
              tankMetaData.Weir_Len_m = dicts["Weir_Len_m"]
              tankMetaData.No_Sluice = dicts["No_Sluice"]
              tankMetaData.Low_Sil_m = dicts["Low_Sil_m"]
              tankMetaData.Bund_Len_m = dicts["Bund_Len_m"]
              tankMetaData.Dis_cusec = dicts["Dis_cusec"]
              tankMetaData.save()
              serializer = TankMetaDataSerializer(tankMetaData)
              return Response(serializer.data)
            

          serializer = TankImageSerializer(tank_image)
          return Response(serializer.data)


    






    