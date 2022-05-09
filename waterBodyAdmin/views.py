from pickle import FALSE, TRUE
import os
import logging
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
from django.views.generic import TemplateView

from waterbody.settings import BASE_DIR
from .models import Block, Month, Panchayat, Role, SurveyQuestionMetaData, Taluk, TankImage, TankMetaData, UserProfile, WaterBodyAyacutNonCultivation, WaterBodyBoundaryDropPoint, WaterBodyBund, WaterBodyCropping, WaterBodyCrossSection, WaterBodyDepthSillLevel, WaterBodyExoticSpecies, WaterBodyFamilyDistributionLand, WaterBodyFamilyNature, WaterBodyFenceCondition, WaterBodyFenceType, WaterBodyGhatCondition, WaterBodyInletType, WaterBodyInvestmentNature, WaterBodyIrrigationTankFunction, WaterBodyMWLStone, WaterBodyOoraniFunction, WaterBodyOutletType, WaterBodyOwnerShip, WaterBodyShutter, WaterBodyShutterCondition, WaterBodySlitTrap, WaterBodySluice, WaterBodySluiceCondition, WaterBodySource, WaterBodyStonePitching, WaterBodyStonePitchingCondition, WaterBodyStreamIssues, WaterBodySurplusWeir, WaterBodyTankIssues, WaterBodyTankUniqueness, WaterBodyTempleTankType, WaterBodyType
from .serializers import BlockSerializer, MonthSerializer, PanchayatSerializer, RoleSerializer, RoleUpdateSerializer, SurveyQuestionDataSerializer, \
     TalukSerializer, TankImageSerializer, TankMetaDataSerializer, UserProfileAddSerializer, UserProfileSerializer, \
     UserProfileUpdateSerializer, WaterBodyAyacutNonCultivationSerializer, WaterBodyBoundaryDropPointSerializer, WaterBodyBundSerializer, WaterBodyCroppingSerializer, WaterBodyCrossSectionSerializer, WaterBodyDepthSillLevelSerializer, WaterBodyExoticSpeciesSerializer, WaterBodyFamilyDistributionLandSerializer, WaterBodyFamilyNatureSerializer, WaterBodyFenceConditionSerializer, WaterBodyFenceTypeSerializer, WaterBodyGhatConditionSerializer, WaterBodyInletTypeSerializer, WaterBodyInvestmentNatureSerializer, WaterBodyIrrigationTankFunctionSerializer, WaterBodyMWLStoneSerializer, WaterBodyOoraniFunctionSerializer, WaterBodyOutletTypeSerializer, WaterBodyOwnerShipSerializer, WaterBodyShutterConditionSerializer, WaterBodyShutterSerializer, WaterBodySlitTrapSerializer, WaterBodySluiceConditionSerializer, WaterBodySluiceSerializer, WaterBodySourceSerializer, WaterBodyStonePitchingConditionSerializer, WaterBodyStonePitchingSerializer, WaterBodyStreamIssuesSerializer, WaterBodySurplusWeirSerializer, WaterBodyTankIssuesSerializer, WaterBodyTankUniquenessSerializer, WaterBodyTempleTankTypeSerializer, WaterBodyTypeSerializer

logger = logging.getLogger(__name__)

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html" #your_template

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

class TalukViewSet(ModelViewSet):
    logger.info('Calling Taluk View Set')
    http_method_names = ['get','post','patch','delete']
    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        logger.info('Retriving All Taluks')
        queryset = Taluk.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class BlockViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = Block.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class PanchayatViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = Panchayat.objects.all()
    serializer_class = PanchayatSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def AllPanchayatsByBlockId(self,request):
        # get query params from get request
        id = request.query_params["blockId"]
        queryset = Panchayat.objects.filter(blockId_id=id).values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyTypeViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyType.objects.all()
    serializer_class = WaterBodyTypeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyType.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyOwnerShipViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyOwnerShip.objects.all()
    serializer_class = WaterBodyOwnerShipSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyOwnerShip.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class MonthViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = Month.objects.all()
    serializer_class = MonthSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = Month.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodySourceViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodySource.objects.all()
    serializer_class = WaterBodySourceSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodySource.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyCrossSectionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyCrossSection.objects.all()
    serializer_class = WaterBodyCrossSectionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyCrossSection.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyStreamIssuesViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyStreamIssues.objects.all()
    serializer_class = WaterBodyStreamIssuesSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyStreamIssues.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyExoticSpeciesViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyExoticSpecies.objects.all()
    serializer_class = WaterBodyExoticSpeciesSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyExoticSpecies.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyBundViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyBund.objects.all()
    serializer_class = WaterBodyBundSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyBund.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyTankIssuesViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyTankIssues.objects.all()
    serializer_class = WaterBodyTankIssuesSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyTankIssues.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyStonePitchingViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyStonePitching.objects.all()
    serializer_class = WaterBodyStonePitchingSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyStonePitching.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyStonePitchingConditionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyStonePitchingCondition.objects.all()
    serializer_class = WaterBodyStonePitchingConditionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyStonePitchingCondition.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodySluiceViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodySluice.objects.all()
    serializer_class = WaterBodySluiceSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodySluice.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyDepthSillLevelViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyDepthSillLevel.objects.all()
    serializer_class = WaterBodyDepthSillLevelSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyDepthSillLevel.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyShutterViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyShutter.objects.all()
    serializer_class = WaterBodyShutterSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyShutter.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyConditionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodySluiceCondition.objects.all()
    serializer_class = WaterBodySluiceConditionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodySluiceCondition.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyShutterConditionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyShutterCondition.objects.all()
    serializer_class = WaterBodyShutterConditionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyShutterCondition.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodySurplusWeirViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodySurplusWeir.objects.all()
    serializer_class = WaterBodySurplusWeirSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodySurplusWeir.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyMWLStoneViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyMWLStone.objects.all()
    serializer_class = WaterBodyMWLStoneSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyMWLStone.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyIrrigationTankFunctionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyIrrigationTankFunction.objects.all()
    serializer_class = WaterBodyIrrigationTankFunctionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyIrrigationTankFunction.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyAyacutNonCultivationViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyAyacutNonCultivation.objects.all()
    serializer_class = WaterBodyAyacutNonCultivationSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyAyacutNonCultivation.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyCroppingViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyCropping.objects.all()
    serializer_class = WaterBodyCroppingSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyCropping.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyInvestmentNatureViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyInvestmentNature.objects.all()
    serializer_class = WaterBodyInvestmentNatureSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyInvestmentNature.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyFamilyNatureViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyFamilyNature.objects.all()
    serializer_class = WaterBodyFamilyNatureSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyFamilyNature.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyFamilyDistributionLandViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyFamilyDistributionLand.objects.all()
    serializer_class = WaterBodyFamilyDistributionLandSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyFamilyDistributionLand.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyTankUniquenessViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyTankUniqueness.objects.all()
    serializer_class = WaterBodyTankUniquenessSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyTankUniqueness.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyBoundaryDropPointViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyBoundaryDropPoint.objects.all()
    serializer_class = WaterBodyBoundaryDropPointSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyBoundaryDropPoint.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyTypeViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyType.objects.all()
    serializer_class = WaterBodyTypeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyType.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyTempleTankTypeViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyTempleTankType.objects.all()
    serializer_class = WaterBodyTempleTankTypeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyTempleTankType.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyInletTypeViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyInletType.objects.all()
    serializer_class = WaterBodyInletTypeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyInletType.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodySlitTrapViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodySlitTrap.objects.all()
    serializer_class = WaterBodySlitTrapSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodySlitTrap.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyOutletTypeViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyOutletType.objects.all()
    serializer_class = WaterBodyOutletTypeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyOutletType.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyGhatConditionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyGhatCondition.objects.all()
    serializer_class = WaterBodyGhatConditionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyGhatCondition.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyFenceConditionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyFenceCondition.objects.all()
    serializer_class = WaterBodyFenceConditionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyFenceCondition.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class WaterBodyFenceTypeViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset = WaterBodyFenceType.objects.all()
    serializer_class = WaterBodyFenceTypeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset = WaterBodyFenceType.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))

class  WaterBodyOoraniFunctionViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    queryset =  WaterBodyOoraniFunction.objects.all()
    serializer_class = WaterBodyOoraniFunctionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    search_fields = ( 'name' )
    ordering_fields = [ 'name' ]

    @action(detail=False, methods=['GET'])
    def All(self,request):
        queryset =  WaterBodyOoraniFunction.objects.values('id','name')
        if request.method == 'GET':
            return Response(list(queryset))


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


    






    