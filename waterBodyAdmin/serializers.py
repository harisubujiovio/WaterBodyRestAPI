import os
from pickle import FALSE, TRUE
from rest_framework import serializers
from .models import AccessRights, AccessRightsPermissions, Block, District, Month, Panchayat, PermissionType, Resource, ResourcePermission, Section, SectionQuestion, SurveyQuestionMetaData, Taluk, TankImage, TankMetaData, UserProfile, WaterBodyAvailability, WaterBodyAyacutNonCultivation, WaterBodyBarrelType, WaterBodyBedNature, WaterBodyBoundaryDropPoint, WaterBodyBund, WaterBodyBundFunctionalites, WaterBodyBundIssues, WaterBodyBundIssuesResponse, WaterBodyBundResponse, WaterBodyBundStonePitchings, WaterBodyCatchmentType, WaterBodyCropping, WaterBodyCrossSection, WaterBodyDepthSillLevel, WaterBodyDomesticResponse, WaterBodyDrinkingResponse, WaterBodyExoticSpecies, WaterBodyFamilyDistributionLand, WaterBodyFamilyNature, WaterBodyFenceCondition, WaterBodyFenceType, WaterBodyFencingResponse, WaterBodyFieldChannelType, WaterBodyFishingResponse, WaterBodyForLiveStockResponse, WaterBodyForPotteryResponse, WaterBodyFreeCatchmentResponse, WaterBodyFreeCatchmentStreamIssues, WaterBodyFunctionalParameterResponse, WaterBodyGhatCondition, WaterBodyGhatsResponse, WaterBodyHarvestFromBundTreeResponse, WaterBodyHydrologicResponse, WaterBodyHydrologicalPrioritySourceSupply, WaterBodyHydrologicalSourceSupply, WaterBodyInletResponse, WaterBodyInletType, WaterBodyInvestmentNature, WaterBodyIrrigationCanalResponse, WaterBodyIrrigationCanalStreamIssues, WaterBodyIrrigationResponse, WaterBodyIrrigationTankFunction, WaterBodyLotusCultivationResponse, WaterBodyMWLStone, WaterBodyOoraniFunction, WaterBodyOutletResponse, WaterBodyOutletType, WaterBodyOwnerShip, WaterBodyRiverStreamIssues, WaterBodyRiverStreamResponse, WaterBodySectionType, WaterBodyShutter, WaterBodyShutterCondition, WaterBodySlitTrap, WaterBodySluice, WaterBodySluiceCondition, WaterBodySluiceResponse, WaterBodySource, WaterBodySource1Response, WaterBodySpreadAreaIssues, WaterBodySpreadInvasiveSpecies, WaterBodySpreadIssues, WaterBodySpreadResponse, WaterBodySpringResponse, WaterBodyStonePitching, WaterBodyStonePitchingCondition, WaterBodyStreamIssues, WaterBodySubSurfaceResponse, WaterBodySupplySource1Response, WaterBodySurPlusSluiceFromUpperTankResponse, WaterBodySurpluCoarseIssues, WaterBodySurpluCoarseResponse, WaterBodySurplusWeir, WaterBodySurplusweirResponse, WaterBodySurveyResponse, WaterBodyTankBedCultivationResponse, WaterBodyTankBedDistributionLands, WaterBodyTankBedFamilies, WaterBodyTankIssues, WaterBodyTankType, WaterBodyTankUniqueness, WaterBodyTankUniquenessResponse, WaterBodyTempleTankType, WaterBodyType, WaterBodyUpperTankSluiceResponse, WaterBodyUpperTankSluiceStreamIssues
from .models import Role

class RoleUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id','first_name','last_name','email','mobileNumber','address']



class UserRoleSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Role
        fields = ['id','name']

class RoleSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    users = RoleUserSerializer(many=True,read_only=True)
    class Meta:
        model = Role
        fields = ['id','name','description','createdBy','lastModifiedBy','users']

class RoleDictionarySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Role
        fields = ['id','name']

class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name','description','lastModifiedBy']

class ResourceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Resource
        fields = ['id','name','createdBy']

class PermissionTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = PermissionType
        fields = ['id','name','createdBy']

class ResourcePermissionCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = ResourcePermission
        fields = ['id','resource','permission','createdBy']

class ResourcePermissionListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    resource = ResourceSerializer(many=False,read_only=True)
    permission = PermissionTypeSerializer(many=False,read_only=True)
    class Meta:
        model = ResourcePermission
        fields = ['id','resource','permission','createdBy']

class ResourcePermissionSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)

class AccessRightsSerializer(serializers.Serializer):
    permission_id = serializers.UUIDField(read_only=True)
    resource_id = serializers.UUIDField(read_only=True)
    accessright_id = serializers.UUIDField(read_only=True)
    id = serializers.UUIDField(read_only=True)
    resourcename = serializers.CharField(max_length=255)
    permissionname = serializers.CharField(max_length=255)
    status = serializers.SerializerMethodField(method_name="get_Status")
    
    def get_Status(self, accessRightPermission: AccessRightsPermissions):
             if(accessRightPermission.accessright_id):
                 return True 
             else:
                 return False

class AccessRightsCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = AccessRights
        fields = ['id','createdBy','lastModifiedBy', 'role','resource','permission']

class AccessRightsListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    role = RoleDictionarySerializer(many=False,read_only=True)
    resource = ResourceSerializer(many=False,read_only=True)
    permission = PermissionTypeSerializer(many=False,read_only=True)
    class Meta:
        model = AccessRights
        fields = ['id','createdBy','role','resource','permission']

class TankImageSerializer(serializers.ModelSerializer):
     id = serializers.UUIDField(read_only=True)
    #  filename = serializers.SerializerMethodField(method_name="get_FileName")
    #  def get_FileName(self, tankImage: TankImage):
    #         return os.path.basename(tankImage.image.name)

     class Meta:
        model = TankImage
        fields = ['id','image','createdBy','createdDate','filename']
        
        

class TankMetaDataSerializer(serializers.ModelSerializer):
     class Meta:
        model = TankMetaData
        fields = ['Unique_id','FID','CLUSTER','TANK_NUM','Tank_Name','Latitude','Longitude',
        'Village', 'Block', 'Taluk', 'District','Subbasin', 'Basin', 'Section', 'Sub_Dn',
        'Division', 'Circle', 'Region', 'Tank_Type', 'Cap_MCM','FTL_m', 'MWL_m', 'TBL_m',
        'Sto_Dep_m', 'Ayacut_ha', 'Catch_sqkm', 'Wat_Spr_ha', 'No_of_Weir', 'Weir_Len_m',
        'No_Sluice','Low_Sil_m','Bund_Len_m','Dis_cusec','tankId']

class SurveyQuestionDataSerializer(serializers.ModelSerializer):
     id = serializers.UUIDField(read_only=True)
     createdBy = serializers.UUIDField(read_only=True)
     statusText = serializers.SerializerMethodField(method_name="get_StatusText")
     def get_StatusText(self, question: SurveyQuestionMetaData):
             if(question.status):
                 return 'Active' 
             else:
                 return 'InActive'
     class Meta:
        model = SurveyQuestionMetaData
        fields = ['id','question','status','createdBy','statusText']

        

class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.IntegerField()
    ordering_fields = '__all__'
    class Meta:
        model = UserProfile
        fields = ['id','user_id','username','first_name','last_name','email','mobileNumber','address','role','pincode']

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.IntegerField()
    role = UserRoleSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id','user_id','first_name','last_name','email','mobileNumber','address','role','pincode']

class UserProfileAddSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.IntegerField()
    class Meta:
        model = UserProfile
        fields = ['id','user_id','mobileNumber','address','role',
        'district','division','region','block','state','pincode']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','mobileNumber','address','role',
        'district','division','region','block','state','pincode']

class TalukSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Taluk
        fields = ['id','code', 'name','createdBy','lastModifiedBy']

class DistrictSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = District
        fields = ['id','code','name', 'createdBy','lastModifiedBy']

class BlockSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Block
        fields = ['id','code','name','districtname', 'createdBy','lastModifiedBy']

class PanchayatSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Panchayat
        fields = ['id','code','block','blockname', 'name','createdBy','lastModifiedBy']

class WaterBodyTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyOwnerShipSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyOwnerShip
        fields = ['id','name','createdBy','lastModifiedBy']

class MonthSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Month
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodySourceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySource
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyCrossSectionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyCrossSection
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyStreamIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyStreamIssues
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyExoticSpeciesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyExoticSpecies
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyBundSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBund
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyTankIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankIssues
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyStonePitchingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyStonePitching
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyStonePitchingConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyStonePitchingCondition
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodySluiceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySluice
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyDepthSillLevelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyDepthSillLevel
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyShutterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyShutter
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodySluiceConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySluiceCondition
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyShutterConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyShutterCondition
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodySurplusWeirSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySurplusWeir
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyMWLStoneSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyMWLStone
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyIrrigationTankFunctionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyIrrigationTankFunction
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyAyacutNonCultivationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyAyacutNonCultivation
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyCroppingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyCropping
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyInvestmentNatureSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyInvestmentNature
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyFamilyNatureSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFamilyNature
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyFamilyDistributionLandSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFamilyDistributionLand
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyTankUniquenessSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankUniqueness
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyBoundaryDropPointSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBoundaryDropPoint
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyTempleTankTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTempleTankType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyInletTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyInletType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodySlitTrapSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySlitTrap
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyOutletTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyOutletType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyGhatConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyGhatCondition
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyBedNatureSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBedNature
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyTankTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyAvailabilitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyAvailability
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyCatchmentTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyCatchmentType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyFenceConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFenceCondition
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyFenceTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFenceType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyOoraniFunctionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyOoraniFunction
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyBundIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBundIssues
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyBarrelTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBarrelType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodyFieldChannelTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFieldChannelType
        fields = ['id','name','createdBy','lastModifiedBy']

class WaterBodySpreadIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySpreadIssues
        fields = ['id','name','createdBy','lastModifiedBy']

class SectionQuestionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = SectionQuestion
        fields = ['id','name','section','fieldType','createdBy','lastModifiedBy']

class SectionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    questions = SectionQuestionSerializer(many=True,read_only=True)
    class Meta:
        model = Section
        fields = ['id','name','createdBy','lastModifiedBy','questions']

class WaterBodySectionTypePostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySectionType
        fields = ['id','section','waterbodytype','createdBy','lastModifiedBy']

class WaterBodySectionTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    section = SectionSerializer(many=False,read_only=True)
    class Meta:
        model = WaterBodySectionType
        fields = ['id','section','waterbodytype','createdBy','lastModifiedBy']

class ChartDataSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    data = serializers.DecimalField(max_digits=6,decimal_places=2)

class CardSummarySerializer(serializers.Serializer):
    label = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    data = serializers.DecimalField(max_digits=6,decimal_places=2)
    filterKey = serializers.CharField(max_length=255)
    icon = serializers.CharField(max_length=255)

class JSONSectionQuestionSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=255)
    section = serializers.UUIDField()
    response = serializers.CharField(max_length=255)
   
class JSONSectionSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=255)
    questions = JSONSectionQuestionSerializer(many=TRUE)


class SurveyResponseSerializer(serializers.Serializer):
     id = serializers.UUIDField()
     section = JSONSectionSerializer(many=False)


class SurveyResponseListSerializer(serializers.Serializer):
     responses = serializers.ListField(child=SurveyResponseSerializer())

     def save(self, **kwargs):
         list = self.validated_data['responses']
         for surveyList in list:
           for key, value in surveyList.items():
              print(key, value)

# class WaterBodySurveyResponseSerializer(serializers.Serializer):
#     waterbodytype = serializers.UUIDField(read_only=True)
#     section = serializers.ListField()

#     def save(self, **kwargs):
#          print(self.validated_data['waterbodytype'])

# class WaterSpreadAreaIssueResponseSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(read_only=True)
#     class Meta:
#         model = WaterSpreadAreaIssueResponse
#         fields = ['id','createdBy']

class WaterBodyDrinkingResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyDrinkingResponse
        fields = ['id','surveyResponse','dependentfamiliesnumber', 'dugwellnumber','depthofdugwell',
        'dugwellcondition','numberofborewells', 'depthofborewell',
        'borewellcondition','createdBy']

class WaterBodyDomesticResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyDomesticResponse
        fields = ['id','surveyResponse','dependentfamiliesnumber','dependentlivestocksnumber',
         'dugwellnumber','depthofdugwell','dugwellcondition','numberofborewells', 'depthofborewell',
          'borewellcondition','createdBy']

class WaterBodyFencingResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFencingResponse
        fields = ['id','surveyResponse','fencetype','fencecondition','createdBy']

class WaterBodyGhatsResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyGhatsResponse
        fields = ['id','surveyResponse','ghatnumber','ghatcondition','numberofghatsneeded','createdBy']

class WaterBodyOutletResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyOutletResponse
        fields = ['id','surveyResponse','outletnumber','outlettype','outletcondition','createdBy']

class WaterBodyInletResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyInletResponse
        fields = ['id','surveyResponse','inletnumber','inlettype','inletcondition',
         'slittrap','createdBy']

class WaterBodyForLiveStockResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyForLiveStockResponse
        fields = ['id','surveyResponse', 'dependentfamiliesnumber','dependentanimalssnumber','createdBy']

class WaterBodyForPotteryResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyForPotteryResponse
        fields = ['id','surveyResponse', 'dependentfamiliesnumber','createdBy']

class WaterBodyHarvestFromBundTreeResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyHarvestFromBundTreeResponse
        fields = ['id','surveyResponse', 'investmentnature', 'monthofrelease','monthofharvest',
         'investment','returns', 'dependentfamiliesnumber','createdBy']

class WaterBodyTankBedDistributionLandsSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    tankBedResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankBedDistributionLands
        fields = ['id','tankBedResponse', 'distributionLand','createdBy']

class WaterBodyWaterBodyTankBedFamiliesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    tankBedResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankBedFamilies
        fields = ['id','tankBedResponse', 'family','createdBy']

class WaterBodyTankBedCultivationResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Families = WaterBodyWaterBodyTankBedFamiliesSerializer(many=True)
    DistributionLands = WaterBodyTankBedDistributionLandsSerializer(many=True)
    class Meta:
        model = WaterBodyTankBedCultivationResponse
        fields = ['id','surveyResponse', 'area', 'dependentfamiliesnumber','monthofrelease', 'monthofharvest',
         'investment','returns','Families','DistributionLands', 'createdBy']

    def create(self, validated_data):
        Families = validated_data.pop('Families')
        DistributionLands = validated_data.pop('DistributionLands')
        tankbedCultivation_response = WaterBodyTankBedCultivationResponse.objects.create(**validated_data)
        for family in Families:
            WaterBodyTankBedFamilies.objects.create(tankBedResponse=tankbedCultivation_response,**family)
        for land in DistributionLands:
            WaterBodyTankBedDistributionLands.objects.create(tankBedResponse=tankbedCultivation_response,**land)
        return tankbedCultivation_response

class WaterBodyLotusCultivationResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyLotusCultivationResponse
        fields = ['id','surveyResponse', 'investmentnature', 'monthofrelease','monthofharvest',
         'investment','returns', 'dependentfamiliesnumber','createdBy']

class WaterBodyFishingResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFishingResponse
        fields = ['id','surveyResponse', 'investmentnature', 'monthofrelease','monthofharvest',
         'investment','returns', 'dependentfamiliesnumber','createdBy']

class WaterBodyIrrigationResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyIrrigationResponse
        fields = ['id','surveyResponse', 'ayacutcultivation', 'ayacutnature','cropping',
         'firstcropname','secondcropname', 'thirdcropname','dugwellnumber','depthofdugwell',
         'borewellnumber','maxborewelldepth','dependentfamiliesnumber','createdBy']

class WaterBodySurpluCoarseIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    surpluCoarseResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySurpluCoarseIssues
        fields = ['id','surpluCoarseResponse', 'issue','createdBy']

class WaterBodySurpluCoarseResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Issues = WaterBodySurpluCoarseIssuesSerializer(many=True)
    class Meta:
        model = WaterBodySurpluCoarseResponse
        fields = ['id','surveyResponse', 'tankName', 'streamtype','actualbreadth',
         'currentbreadth','actualbottomwidth', 'currentbottomwidth','actualdepth','currentdepth','Issues',
         'createdBy']

    def create(self, validated_data):
        Issues = validated_data.pop('Issues')
        surpluCoarse_response = WaterBodySurpluCoarseResponse.objects.create(**validated_data)
        for issue in Issues:
            WaterBodySurpluCoarseIssues.objects.create(surpluCoarseResponse=surpluCoarse_response,**issue)
        return surpluCoarse_response

class WaterBodySurplusweirResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySurplusweirResponse
        fields = ['id','surveyResponse', 'surplusweirnumber', 'surplusweirtype','surplusweirLength',
         'silllevelDepth','mwlstones', 'mwlstonedepth','leveldifference','shutterType',
         'surplusweircondition','createdBy']

class WaterBodySluiceResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySluiceResponse
        fields = ['id','surveyResponse', 'sluicenumber', 'sluicetype','sluiceIrrigatedArea',
         'silllevelDepth','shutterType', 'sluicecondition','shuttercondition',
         'sluicefeedanywaterbody','waterbodyname', 'createdBy']

class WaterBodyBundStonePitchingsSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    bundResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBundStonePitchings
        fields = ['id','bundResponse', 'stonePitching','createdBy']

class WaterBodyBundFunctionalitesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    bundResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBundFunctionalites
        fields = ['id','bundResponse', 'bundfunctionality','createdBy']

class WaterBodyBundIssuesResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    bundResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBundIssuesResponse
        fields = ['id','bundResponse', 'issue','createdBy']

class WaterBodyBundResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    BundIssues = WaterBodyBundIssuesSerializer(many=True)
    Functionalites = WaterBodyBundFunctionalitesSerializer(many=True)
    Pitchings = WaterBodyBundStonePitchingsSerializer(many=True)
    class Meta:
        model = WaterBodyBundResponse
        fields = ['id','surveyResponse', 'bundlength','bundtopwidth' ,'slopefrontside',
         'sloperearside', 'stonepitchingcondition', 'revetmentlength',
         'BundIssues','Functionalites', 'Pitchings', 'createdBy']

    def create(self, validated_data):
        Issues = validated_data.pop('BundIssues')
        Functionalites = validated_data.pop('Functionalites')
        Pitchings = validated_data.pop('Pitchings')
        bund_response = WaterBodyBundResponse.objects.create(**validated_data)
        for issue in Issues:
            WaterBodyBundIssues.objects.create(bundResponse=bund_response,**issue)
        for functionality in Functionalites:
            WaterBodyBundFunctionalites.objects.create(bundResponse=bund_response,**functionality)
        for pitching in Pitchings:
            WaterBodyBundStonePitchings.objects.create(bundResponse=bund_response,**pitching)
        return bund_response

class WaterBodySurPlusSluiceFromUpperTankSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySurPlusSluiceFromUpperTankResponse
        fields = ['id','surveyResponse','tankName','contributiontypepercentage',
        'seassonstart','seassonend','createdBy']

class WaterBodyUpperTankSluiceStreamIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    upperTankSluiceResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyUpperTankSluiceStreamIssues
        fields = ['id','upperTankSluiceResponse', 'issue','createdBy']

class WaterBodyUpperTankSluiceResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Issues = WaterBodyUpperTankSluiceStreamIssuesSerializer(many=True)
    class Meta:
        model = WaterBodyUpperTankSluiceResponse
        fields = ['id','surveyResponse','tankName','contributionpercentage',
        'seassonstart','seassonend','streamtype','streamheadtopwidth','streamheadbed',
        'streamheaddepth','streammiddletopwidth','streammiddlebed','streammiddledepth',
        'streamtailendtopwidth','streamtailendbed','streamtailenddepth', 'Issues','createdBy']

    def create(self, validated_data):
        Issues = validated_data.pop('Issues')
        sluice_response = WaterBodyUpperTankSluiceResponse.objects.create(**validated_data)
        for issue in Issues:
            WaterBodyUpperTankSluiceStreamIssues.objects.create(upperTankSluiceResponse=sluice_response,**issue)
        return sluice_response

    def update(self, instance, validated_data):
        Issues = validated_data.pop('Issues')
        if Issues is not None:
            WaterBodyUpperTankSluiceStreamIssues.objects.filter(upperTankSluiceResponse_id=instance.id).delete()
            if len(Issues) > 0:
                for issue in Issues:
                    WaterBodyUpperTankSluiceStreamIssues.objects.create(upperTankSluiceResponse=instance,**issue)
        tankName = self.validated_data.get("tankName")
        if tankName is not None:
           instance.tankName = tankName
        contributiontypepercentage = self.validated_data.get("contributiontypepercentage")
        if contributiontypepercentage is not None:
           instance.contributiontypepercentage = contributiontypepercentage
        seassonstart = self.validated_data.get("seassonstart")
        if seassonstart is not None:
           instance.seassonstart = seassonstart
        seassonend = self.validated_data.get("seassonend")
        if seassonend is not None:
           instance.seassonend = seassonend
        streamtype = self.validated_data.get("streamtype")
        if streamtype is not None:
           instance.streamtype = streamtype
        streamheadtopwidth = self.validated_data.get("streamheadtopwidth")
        if streamheadtopwidth is not None:
           instance.streamheadtopwidth = streamheadtopwidth
        streamheadbed = self.validated_data.get("streamheadbed")
        if streamheadbed is not None:
           instance.streamheadbed = streamheadbed
        streamheaddepth = self.validated_data.get("streamheaddepth")
        if streamheaddepth is not None:
           instance.streamheaddepth = streamheaddepth
        streammiddletopwidth = self.validated_data.get("streammiddletopwidth")
        if streammiddletopwidth is not None:
           instance.streammiddletopwidth = streammiddletopwidth
        streammiddlebed = self.validated_data.get("streammiddlebed")
        if streammiddlebed is not None:
           instance.streammiddlebed = streammiddlebed
        streammiddledepth = self.validated_data.get("streammiddledepth")
        if streammiddledepth is not None:
           instance.streammiddlebed = streammiddledepth
        streamtailendtopwidth = self.validated_data.get("streamtailendtopwidth")
        if streamtailendtopwidth is not None:
           instance.streammiddlebed = streamtailendtopwidth
        streamtailendbed = self.validated_data.get("streamtailendbed")
        if streamtailendbed is not None:
           instance.streamtailendbed = streamtailendbed
        streamtailenddepth = self.validated_data.get("streamtailenddepth")
        if streamtailenddepth is not None:
           instance.streamtailenddepth = streamtailenddepth
        lastModifiedBy = self.validated_data.get("lastModifiedBy")
        if lastModifiedBy is not None:
           instance.lastModifiedBy = lastModifiedBy
        instance.save()
        return instance

class WaterBodyRiverStreamIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    spreadResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyRiverStreamIssues
        fields = ['id','spreadResponse', 'issue','createdBy']

class WaterBodyRiverStreamResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Issues = WaterBodyRiverStreamIssuesSerializer(many=True)
    class Meta:
        model = WaterBodyRiverStreamResponse
        fields = ['id','surveyResponse','riverName',
        'bednature','seassonstart','seassonend','contributiontypepercentage',
        'streamtype','streamtopwidth','streambed','streamdepth', 'Issues','createdBy']

    def create(self, validated_data):
        Issues = validated_data.pop('Issues')
        riverstream_response = WaterBodyRiverStreamResponse.objects.create(**validated_data)
        for issue in Issues:
            WaterBodyRiverStreamIssues.objects.create(riverStreamResponse=riverstream_response,**issue)
        return riverstream_response

    def update(self, instance, validated_data):
        Issues = validated_data.pop('Issues')
        if Issues is not None:
            WaterBodyRiverStreamIssues.objects.filter(riverStreamResponse_id=instance.id).delete()
            if len(Issues) > 0:
                for issue in Issues:
                    WaterBodyRiverStreamIssues.objects.create(riverStreamResponse=instance,**issue)
        riverName = self.validated_data.get("riverName")
        if riverName is not None:
           instance.riverName = riverName
        bednature = self.validated_data.get("bednature")
        if bednature is not None:
           instance.bednature = bednature
        seassonstart = self.validated_data.get("seassonstart")
        if seassonstart is not None:
           instance.seassonstart = seassonstart
        seassonend = self.validated_data.get("seassonend")
        if seassonend is not None:
           instance.seassonend = seassonend
        streamtype = self.validated_data.get("streamtype")
        if streamtype is not None:
           instance.streamtype = streamtype
        contributiontypepercentage = self.validated_data.get("contributiontypepercentage")
        if contributiontypepercentage is not None:
           instance.contributiontypepercentage = contributiontypepercentage
        streamtopwidth = self.validated_data.get("streamtopwidth")
        if streamtopwidth is not None:
           instance.streamtopwidth = streamtopwidth
        streambed = self.validated_data.get("streambed")
        if streambed is not None:
           instance.streambed = streambed
        streamdepth = self.validated_data.get("streamdepth")
        if streamdepth is not None:
           instance.streamdepth = streamdepth
        lastModifiedBy = self.validated_data.get("lastModifiedBy")
        if lastModifiedBy is not None:
           instance.lastModifiedBy = lastModifiedBy
        instance.save()
        return instance

class WaterBodySpringResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySpringResponse
        fields = ['id','surveyResponse','numberofspring','springnature',
        'seassonstart','seassonend','contributiontypepercentage','createdBy']

class WaterBodySubSurfaceResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySubSurfaceResponse
        fields = ['id','surveyResponse','numberofspring','springnature',
        'seassonstart','seassonend','contributiontypepercentage','createdBy']


class WaterBodySpreadAreaIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    spreadResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySpreadAreaIssues
        fields = ['id','spreadResponse', 'issue','createdBy']

class WaterBodySpreadInvasiveSpeciesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    spreadResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySpreadInvasiveSpecies
        fields = ['id','spreadResponse', 'specie','createdBy']


class WaterBodySpreadResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    SpreadAreaIssues = WaterBodySpreadAreaIssuesSerializer(many=True)
    SpreadAreaSpecies = WaterBodySpreadInvasiveSpeciesSerializer(many=True)
    class Meta:
        model = WaterBodySpreadResponse
        fields = ['id','surveyResponse', 'spreadpercentage','SpreadAreaIssues', 'SpreadAreaSpecies','createdBy']

    def create(self, validated_data):
        SpreadAreaIssues = validated_data.pop('SpreadAreaIssues')
        SpreadAreaSpecies = validated_data.pop('SpreadAreaSpecies')
        spread_response = WaterBodySpreadResponse.objects.create(**validated_data)
        for issue in SpreadAreaIssues:
            WaterBodySpreadAreaIssues.objects.create(spreadResponse=spread_response,**issue)
        for specie in SpreadAreaSpecies:
            WaterBodySpreadInvasiveSpecies.objects.create(spreadResponse=spread_response,**specie)
        return spread_response

    def update(self, instance, validated_data):
        SpreadAreaIssues = validated_data.pop('SpreadAreaIssues')
        SpreadAreaSpecies = validated_data.pop('SpreadAreaSpecies')
        if SpreadAreaIssues is not None:
            WaterBodySpreadAreaIssues.objects.filter(spreadResponse_id=instance.id).delete()
            if len(SpreadAreaIssues) > 0:
                for issue in SpreadAreaIssues:
                    WaterBodySpreadAreaIssues.objects.create(spreadResponse=instance,**issue)
        if SpreadAreaSpecies is not None:
            WaterBodySpreadInvasiveSpecies.objects.filter(spreadResponse_id=instance.id).delete()
            if len(SpreadAreaSpecies) > 0:
                for specie in SpreadAreaSpecies:
                    WaterBodySpreadInvasiveSpecies.objects.create(spreadResponse=instance,**specie)
        spreadpercentage = self.validated_data.get("spreadpercentage")
        if spreadpercentage is not None:
           instance.spreadpercentage = spreadpercentage
        lastModifiedBy = self.validated_data.get("lastModifiedBy")
        if lastModifiedBy is not None:
           instance.lastModifiedBy = lastModifiedBy
        instance.save()
        return instance



class WaterBodyFreeCatchmentStreamIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    freeCatchmentResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFreeCatchmentStreamIssues
        fields = ['id','freeCatchmentResponse', 'issue','createdBy']

class WaterBodyIrrigationCanalStreamIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    irrigationCanalResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyIrrigationCanalStreamIssues
        fields = ['id','irrigationCanalResponse', 'issue','createdBy']

class WaterBodyIrrigationCanalResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Issues = WaterBodyIrrigationCanalStreamIssuesSerializer(many=True)
    class Meta:
        model = WaterBodyIrrigationCanalResponse
        fields = ['id','surveyResponse', 'canalName','bednature','numberofSupplies', 
        'firstseassonstart', 'firstseassonend', 'secondseassonstart', 'secondseassonend', 'contributiontypepercentage',
        'streamtype','streamtopwidth','streambed', 'streamdepth','Issues','createdBy']

    def create(self, validated_data):
        Issues = validated_data.pop('Issues')
        irrigationcanal_response = WaterBodyIrrigationCanalResponse.objects.create(**validated_data)
        for issue in Issues:
            WaterBodyIrrigationCanalStreamIssues.objects.create(irrigationCanalResponse=irrigationcanal_response,**issue)
        return irrigationcanal_response

    def update(self, instance, validated_data):
        Issues = validated_data.pop('Issues')
        if Issues is not None:
            WaterBodyIrrigationCanalStreamIssues.objects.filter(irrigationCanalResponse_id=instance.id).delete()
            if len(Issues) > 0:
                for issue in Issues:
                    WaterBodyIrrigationCanalStreamIssues.objects.create(irrigationCanalResponse=instance,**issue)
        canalName = self.validated_data.get("canalName")
        if canalName is not None:
           instance.canalName = canalName
        bednature = self.validated_data.get("bednature")
        if bednature is not None:
           instance.bednature = bednature
        numberofSupplies = self.validated_data.get("numberofSupplies")
        if numberofSupplies is not None:
           instance.numberofSupplies = numberofSupplies
        firstseassonstart = self.validated_data.get("firstseassonstart")
        if firstseassonstart is not None:
           instance.firstseassonstart = firstseassonstart
        firstseassonend = self.validated_data.get("firstseassonend")
        if firstseassonend is not None:
           instance.firstseassonend = firstseassonend
        secondseassonstart = self.validated_data.get("secondseassonstart")
        if secondseassonstart is not None:
           instance.secondseassonstart = secondseassonstart
        secondseassonend = self.validated_data.get("secondseassonend")
        if secondseassonend is not None:
           instance.secondseassonend = secondseassonend
        contributiontypepercentage = self.validated_data.get("contributiontypepercentage")
        if contributiontypepercentage is not None:
           instance.contributiontypepercentage = contributiontypepercentage
        streamtype = self.validated_data.get("streamtype")
        if streamtype is not None:
           instance.streamtype = streamtype
        streamtopwidth = self.validated_data.get("streamtopwidth")
        if streamtopwidth is not None:
           instance.streamtopwidth = streamtopwidth
        streambed = self.validated_data.get("streambed")
        if streambed is not None:
           instance.streambed = streambed
        streamdepth = self.validated_data.get("streamdepth")
        if streamdepth is not None:
           instance.streamdepth = streamdepth
        lastModifiedBy = self.validated_data.get("lastModifiedBy")
        if lastModifiedBy is not None:
           instance.lastModifiedBy = lastModifiedBy
        instance.save()
        return instance

class WaterBodyFreeCatchmentResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Issues = WaterBodyFreeCatchmentStreamIssuesSerializer(many=True)
    class Meta:
        model = WaterBodyFreeCatchmentResponse
        fields = ['id','surveyResponse','contributiontypepercentage','seassonstart', 
        'seassonend','streamtype','streamheadtopwidth','streamheadbed','streamheaddepth',
        'streammiddletopwidth','streammiddlebed','streammiddledepth','streamtailendtopwidth',
        'streamtailendbed','streamtailenddepth','Issues','createdBy']

    def create(self, validated_data):
        Issues = validated_data.pop('Issues')
        freeCatchment_response = WaterBodyFreeCatchmentResponse.objects.create(**validated_data)
        for issue in Issues:
            WaterBodyFreeCatchmentStreamIssues.objects.create(freeCatchmentResponse=freeCatchment_response,**issue)
        return freeCatchment_response

    def update(self, instance, validated_data):
        Issues = validated_data.pop('Issues')
        if Issues is not None:
            WaterBodyFreeCatchmentStreamIssues.objects.filter(freeCatchmentResponse_id=instance.id).delete()
            if len(Issues) > 0:
                for issue in Issues:
                    WaterBodyFreeCatchmentStreamIssues.objects.create(freeCatchmentResponse=instance,**issue)
        contributiontypepercentage = self.validated_data.get("contributiontypepercentage")
        if contributiontypepercentage is not None:
           instance.contributiontypepercentage = contributiontypepercentage
        seassonstart = self.validated_data.get("seassonstart")
        if seassonstart is not None:
           instance.seassonstart = seassonstart
        seassonend = self.validated_data.get("seassonend")
        if seassonend is not None:
           instance.seassonend = seassonend
        streamtype = self.validated_data.get("streamtype")
        if streamtype is not None:
           instance.streamtype = streamtype
        streamheadtopwidth = self.validated_data.get("streamheadtopwidth")
        if streamheadtopwidth is not None:
           instance.streamheadtopwidth = streamheadtopwidth
        streamheadbed = self.validated_data.get("streamheadbed")
        if streamheadbed is not None:
           instance.streamheadbed = streamheadbed
        streamheaddepth = self.validated_data.get("streamheaddepth")
        if streamheaddepth is not None:
           instance.streamheaddepth = streamheaddepth
        streammiddletopwidth = self.validated_data.get("streammiddletopwidth")
        if streammiddletopwidth is not None:
           instance.streammiddletopwidth = streammiddletopwidth
        streammiddlebed = self.validated_data.get("streammiddlebed")
        if streammiddlebed is not None:
           instance.streammiddlebed = streammiddlebed
        streammiddledepth = self.validated_data.get("streammiddledepth")
        if streammiddledepth is not None:
           instance.streammiddlebed = streammiddledepth
        streamtailendtopwidth = self.validated_data.get("streamtailendtopwidth")
        if streamtailendtopwidth is not None:
           instance.streammiddlebed = streamtailendtopwidth
        streamtailendbed = self.validated_data.get("streamtailendbed")
        if streamtailendbed is not None:
           instance.streamtailendbed = streamtailendbed
        streamtailenddepth = self.validated_data.get("streamtailenddepth")
        if streamtailenddepth is not None:
           instance.streamtailenddepth = streamtailenddepth
        lastModifiedBy = self.validated_data.get("lastModifiedBy")
        if lastModifiedBy is not None:
           instance.lastModifiedBy = lastModifiedBy
        instance.save()
        return instance
        
class WaterBodySource1ResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Source1Response = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySource1Response
        fields = ['id','Source1Response', 'source1','createdBy']

class WaterBodySupplySource1ResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Sources1 = WaterBodySource1ResponseSerializer(many=True)
    class Meta:
        model = WaterBodySupplySource1Response
        fields = ['id','surveyResponse', 'createdBy','Sources1']

    def create(self, validated_data):
        Sources1 = validated_data.pop('Sources1')
        source1suppy_response = WaterBodySupplySource1Response.objects.create(**validated_data)
        for source in Sources1:
            WaterBodySource1Response.objects.create(Source1Response=source1suppy_response,**source)
        return source1suppy_response

    def update(self, instance, validated_data):
        Sources1 = validated_data.pop('Sources1')
        if Sources1 is not None:
            WaterBodySource1Response.objects.filter(Source1Response=instance.id).delete()
            if len(Sources1) > 0:
                for issue in Sources1:
                    WaterBodySource1Response.objects.create(Source1Response=instance,**issue)
        surveyResponse = self.validated_data.get("surveyResponse")
        if surveyResponse is not None:
           instance.surveyResponse = surveyResponse
        lastModifiedBy = self.validated_data.get("lastModifiedBy")
        if lastModifiedBy is not None:
           instance.lastModifiedBy = lastModifiedBy
        instance.save()
        return instance


class WaterBodyHydrologicalSourceSupplySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    hydrologicalResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyHydrologicalSourceSupply
        fields = ['id','hydrologicalResponse', 'source','createdBy']


class WaterBodyHydrologicalPrioritySourceSupplySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    hydrologicalResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyHydrologicalPrioritySourceSupply
        fields = ['id','hydrologicalResponse', 'prioritysource','createdBy']

class WaterBodyHydrologicResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    Sources = WaterBodyHydrologicalSourceSupplySerializer(many=True)
    PrioritySources = WaterBodyHydrologicalPrioritySourceSupplySerializer(many=True)
    class Meta:
        model = WaterBodyHydrologicResponse
        fields = ['id','surveyResponse', 'waterspreadArea','registeredAyacut','capacity','numberoffillings','firstmonthfilling',
            'monthdryup','numberofsources','catchmentType','waterAvailability', 'createdBy',
            'Sources','PrioritySources']

    def create(self, validated_data):
        Sources = validated_data.pop('Sources')
        PrioritySources = validated_data.pop('PrioritySources')
        hydrologic_response = WaterBodyHydrologicResponse.objects.create(**validated_data)
        for source in Sources:
            WaterBodyHydrologicalSourceSupply.objects.create(hydrologicalResponse=hydrologic_response,**source)
        for source in PrioritySources:
            WaterBodyHydrologicalPrioritySourceSupply.objects.create(hydrologicalResponse=hydrologic_response,**source)
        return hydrologic_response

    def update(self, instance, validated_data):
        Sources = validated_data.pop('Sources')
        PrioritySources = validated_data.pop('PrioritySources')
        if Sources is not None:
            WaterBodyHydrologicalSourceSupply.objects.filter(hydrologicalResponse_id=instance.id).delete()
            if len(Sources) > 0:
                for source in Sources:
                    WaterBodyHydrologicalSourceSupply.objects.create(hydrologicalResponse=instance,**source)
        if PrioritySources is not None:
            WaterBodyHydrologicalPrioritySourceSupply.objects.filter(hydrologicalResponse_id=instance.id).delete()
            if len(PrioritySources) > 0:
                for source in PrioritySources:
                    WaterBodyHydrologicalPrioritySourceSupply.objects.create(hydrologicalResponse=instance,**source)
        waterspreadArea = self.validated_data.get("waterspreadArea")
        if waterspreadArea is not None:
           instance.waterspreadArea = waterspreadArea
        registeredAyacut = self.validated_data.get("registeredAyacut")
        if registeredAyacut is not None:
           instance.registeredAyacut = registeredAyacut
        capacity = self.validated_data.get("capacity")
        if capacity is not None:
           instance.capacity = capacity
        numberoffillings = self.validated_data.get("numberoffillings")
        if numberoffillings is not None:
           instance.numberoffillings = numberoffillings
        firstmonthfilling = self.validated_data.get("firstmonthfilling")
        if numberoffillings is not None:
           instance.firstmonthfilling = firstmonthfilling
        monthdryup = self.validated_data.get("monthdryup")
        if monthdryup is not None:
           instance.monthdryup = monthdryup
        numberofsources = self.validated_data.get("numberofsources")
        if numberofsources is not None:
           instance.numberofsources = numberofsources
        catchmentType = self.validated_data.get("catchmentType")
        if catchmentType is not None:
           instance.catchmentType = catchmentType
        waterAvailability = self.validated_data.get("waterAvailability")
        if waterAvailability is not None:
           instance.waterAvailability = waterAvailability
        lastModifiedBy = self.validated_data.get("lastModifiedBy")
        if lastModifiedBy is not None:
           instance.lastModifiedBy = lastModifiedBy
        instance.save()
        return instance
        

class WaterBodyTankUniquenessResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    surveyResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankUniquenessResponse
        fields = ['id','surveyResponse', 'name','createdBy']

class WaterBodyFunctionalParameterResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    surveyResponse = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFunctionalParameterResponse
        fields = ['id','surveyResponse', 'tankFunction','createdBy']

class WaterBodySurveyResponseUpdateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    TankUniqueness = WaterBodyTankUniquenessResponseSerializer(many=TRUE)
    FunctionalParameters = WaterBodyFunctionalParameterResponseSerializer(many=TRUE)
    # BasicDetail = WaterBodyBasicDetailResponseSerializer(many=False)
    # HydrologicParameter = WaterBodyHydrologicResponseSerializer(msany=False)
    # SourceParameter = WaterBodySourceResponseSerializer(many=False)
    # FreeCatchment = WaterBodyFreeCatchmentResponseSerializer(many=False)
    # SluiceUpStream = WaterBodySluiceUpStreamResponseSerializer(many=False)
    # IrrigationCanal = WaterBodyIrrigationCanalResponseSerializer(many=False)
    # WaterbodySpread = WaterBodySpreadResponseSerializer(many=False)
    class Meta:
        model = WaterBodySurveyResponse
        fields = ['id', 'name', 'neerkattipractice', 'legalissue','status', 'createdBy','TankUniqueness','FunctionalParameters']

    def update(self, instance, validated_data):
        print(instance.id)
        TankUniqueness = self.validated_data.get("TankUniqueness")
        FunctionalParameters = self.validated_data.get("FunctionalParameters")
        if TankUniqueness is not None:
            WaterBodyTankUniquenessResponse.objects.filter(surveyResponse_id=instance.id).delete()
            if len(TankUniqueness) > 0:
                for tankUnique in TankUniqueness:
                   WaterBodyTankUniquenessResponse.objects.create(surveyResponse=instance,**tankUnique)
        if FunctionalParameters is not None:
            WaterBodyFunctionalParameterResponse.objects.filter(surveyResponse_id=instance.id).delete()
            if len(FunctionalParameters) > 0:
                for tankfunction in FunctionalParameters:
                   WaterBodyFunctionalParameterResponse.objects.create(surveyResponse=instance,**tankfunction)
        neerkattipractice = self.validated_data.get("neerkattipractice")
        if neerkattipractice is not None:
           instance.neerkattipractice = neerkattipractice
        legalissue = self.validated_data.get("legalissue")
        if legalissue is not None:
           instance.legalissue = legalissue
        status = self.validated_data.get("status")
        if status is not None:
           instance.status = status
        instance.save()
        return instance
        

    # def create(self, validated_data):
    #     TankUniqueness = validated_data.pop('TankUniqueness')
    #     surveyResponse = WaterBodySurveyResponse.objects.create(**validated_data)
    #     for tankUnique in TankUniqueness:
    #         WaterBodyTankUniquenessResponse.objects.create(surveyResponse=surveyResponse,**tankUnique)
    #     return surveyResponse

    # def create(self, validated_data):
    #     print(validated_data)
    #     basicdetail_data = validated_data.pop('BasicDetail')
    #     hydrologicParameter_data = validated_data.pop('HydrologicParameter')
    #     sourceParameter_data = validated_data.pop('SourceParameter')
    #     freeCatchmentParameter_data = validated_data.pop('FreeCatchment')
    #     #surPlusFromUpStreamParameter_data = validated_data.pop('SurPlusFromUpStream')
    #     sluiceUpStreamParameter_data = validated_data.pop('SluiceUpStream')
    #     irrigationCanalParameter_data = validated_data.pop('IrrigationCanal')
    #     #waterbodySpread_data = validated_data.pop('WaterbodySpread')
    #     surveyResponse = WaterBodySurveyResponse.objects.create(**validated_data)
    #     WaterBodyBasicDetailResponse.objects.create(surveyResponse=surveyResponse, **basicdetail_data)
    #     WaterBodyHydrologicResponse.objects.create(surveyResponse=surveyResponse, **hydrologicParameter_data)
    #     WaterBodySourceResponse.objects.create(surveyResponse=surveyResponse, **sourceParameter_data)
    #     WaterBodyFreeCatchmentResponse.objects.create(surveyResponse=surveyResponse, **freeCatchmentParameter_data)
    #     #WaterBodySurPlusFromUpStreamResponse.objects.create(surveyResponse=surveyResponse, **surPlusFromUpStreamParameter_data)
    #     WaterBodySluiceUpStreamResponse.objects.create(surveyResponse=surveyResponse, **sluiceUpStreamParameter_data)
    #     WaterBodyIrrigationCanalResponse.objects.create(surveyResponse=surveyResponse, **irrigationCanalParameter_data)
    #     #WaterBodySpreadResponse.objects.create(surveyResponse=surveyResponse, **waterbodySpread_data)
    #     print(surveyResponse)
    #     return surveyResponse
       

# class WaterBodyGetSurveyResponseSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(read_only=True)
#     class Meta:
#         model = WaterBodySurveyResponse
#         fields = ['id', 'surveyno', 'createdBy']

class WaterBodySurveyResponseAddSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySurveyResponse
        fields = ['id','uniqueid','taluk','block','panchayat',
        'village','surveyno','waterbodytype','ownership',
        'tanktype','status', 'createdBy']

class WaterBodySurveyResponseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    uniqueid = serializers.CharField(max_length=255)
    TankUniqueness = WaterBodyTankUniquenessResponseSerializer(many=TRUE)
    FunctionalParameters = WaterBodyFunctionalParameterResponseSerializer(many=TRUE)
    HydrologicParameter = WaterBodyHydrologicResponseSerializer(many=True)
    # SourceParameter = WaterBodySourceResponseSerializer(many=True)
    FreeCatchment = WaterBodyFreeCatchmentResponseSerializer(many=True)
    IrigationCanal = WaterBodyIrrigationCanalResponseSerializer(many=True)
    Spread = WaterBodySpreadResponseSerializer(many=True)
    Bund = WaterBodyBundResponseSerializer(many=True)
    Sluice = WaterBodySluiceResponseSerializer(many=True)
    Surplusweir = WaterBodySurplusweirResponseSerializer(many=True)
    SurpluCoarse = WaterBodySurpluCoarseResponseSerializer(many=True)
    Irrigation = WaterBodyIrrigationResponseSerializer(many=True)
    Fishing = WaterBodyFishingResponseSerializer(many=True)
    LotusCultivation = WaterBodyLotusCultivationResponseSerializer(many=True)
    TankBedCultivation = WaterBodyTankBedCultivationResponseSerializer(many=True)
    HarvestFromBundTree = WaterBodyHarvestFromBundTreeResponseSerializer(many=True)
    Pottery = WaterBodyForPotteryResponseSerializer(many=True)
    LiveStock = WaterBodyForLiveStockResponseSerializer(many=True)
    Inlets = WaterBodyInletResponseSerializer(many=True)
    Outlets = WaterBodyOutletResponseSerializer(many=True)
    Ghats = WaterBodyGhatsResponseSerializer(many=True)
    Fencings = WaterBodyFencingResponseSerializer(many=True)
    Domestics = WaterBodyDomesticResponseSerializer(many=True)
    Drinkings = WaterBodyDrinkingResponseSerializer(many=True)
    class Meta:
        model = WaterBodySurveyResponse
        fields = ['uniqueid', 'status', 'createdBy','TankUniqueness','FunctionalParameters',
         'BasicDetail','HydrologicParameter', 'SourceParameter',
        'FreeCatchment','SurplusFromUpStream','SluiceUpStream','IrigationCanal','Spread','Bund',
        'Sluice','Surplusweir','SurpluCoarse','Irrigation','Fishing','LotusCultivation',
        'TankBedCultivation','HarvestFromBundTree','Pottery','LiveStock','Inlets','Outlets',
        'Ghats','Fencings','Domestics','Drinkings']




        


