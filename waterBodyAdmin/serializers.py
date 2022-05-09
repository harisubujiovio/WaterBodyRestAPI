import os
from rest_framework import serializers
from .models import Block, Month, Panchayat, SurveyQuestionMetaData, Taluk, TankImage, TankMetaData, UserProfile, WaterBodyAyacutNonCultivation, WaterBodyBoundaryDropPoint, WaterBodyBund, WaterBodyCropping, WaterBodyCrossSection, WaterBodyDepthSillLevel, WaterBodyExoticSpecies, WaterBodyFamilyDistributionLand, WaterBodyFamilyNature, WaterBodyInvestmentNature, WaterBodyIrrigationTankFunction, WaterBodyMWLStone, WaterBodyOwnerShip, WaterBodyShutter, WaterBodyShutterCondition, WaterBodySluice, WaterBodySluiceCondition, WaterBodySource, WaterBodyStonePitching, WaterBodyStonePitchingCondition, WaterBodyStreamIssues, WaterBodySurplusWeir, WaterBodyTankIssues, WaterBodyTankUniqueness, WaterBodyType
from .models import Role

class RoleUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id','first_name','last_name','email','mobileNumber','phoneNumber','address']

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

class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name','description','lastModifiedBy']

class TankImageSerializer(serializers.ModelSerializer):
     id = serializers.UUIDField(read_only=True)
     createdBy = serializers.UUIDField(read_only=True)
     filename = serializers.SerializerMethodField(method_name="get_FileName")
     def get_FileName(self, tankImage: TankImage):
            return os.path.basename(tankImage.image.name)

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
        fields = ['id','user_id','username','first_name','last_name','email','mobileNumber','phoneNumber','address','role']

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.IntegerField()
    role = UserRoleSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id','user_id','first_name','last_name','email','mobileNumber','phoneNumber','address','role']

class UserProfileAddSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.IntegerField()
    class Meta:
        model = UserProfile
        fields = ['id','user_id','mobileNumber','phoneNumber','address','role']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','mobileNumber','phoneNumber','address','role']

class TalukSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Taluk
        fields = ['id','name','createdBy']

class BlockSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Block
        fields = ['id','name','createdBy']

class PanchayatSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Panchayat
        fields = ['id','blockId','name','createdBy']

class WaterBodyTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyType
        fields = ['id','name','createdBy']

class WaterBodyOwnerShipSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyOwnerShip
        fields = ['id','name','createdBy']

class MonthSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Month
        fields = ['id','name','createdBy']

class WaterBodySourceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySource
        fields = ['id','name','createdBy']

class WaterBodyCrossSectionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyCrossSection
        fields = ['id','name','createdBy']

class WaterBodyStreamIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyStreamIssues
        fields = ['id','name','createdBy']

class WaterBodyExoticSpeciesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyExoticSpecies
        fields = ['id','name','createdBy']

class WaterBodyBundSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBund
        fields = ['id','name','createdBy']

class WaterBodyTankIssuesSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankIssues
        fields = ['id','name','createdBy']

class WaterBodyStonePitchingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyStonePitching
        fields = ['id','name','createdBy']

class WaterBodyStonePitchingConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyStonePitchingCondition
        fields = ['id','name','createdBy']

class WaterBodySluiceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySluice
        fields = ['id','name','createdBy']

class WaterBodyDepthSillLevelSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyDepthSillLevel
        fields = ['id','name','createdBy']

class WaterBodyShutterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyShutter
        fields = ['id','name','createdBy']

class WaterBodySluiceConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySluiceCondition
        fields = ['id','name','createdBy']

class WaterBodyShutterConditionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyShutterCondition
        fields = ['id','name','createdBy']

class WaterBodySurplusWeirSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodySurplusWeir
        fields = ['id','name','createdBy']

class WaterBodyMWLStoneSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyMWLStone
        fields = ['id','name','createdBy']

class WaterBodyIrrigationTankFunctionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyIrrigationTankFunction
        fields = ['id','name','createdBy']

class WaterBodyAyacutNonCultivationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyAyacutNonCultivation
        fields = ['id','name','createdBy']

class WaterBodyCroppingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyCropping
        fields = ['id','name','createdBy']

class WaterBodyInvestmentNatureSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyInvestmentNature
        fields = ['id','name','createdBy']

class WaterBodyFamilyNatureSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFamilyNature
        fields = ['id','name','createdBy']

class WaterBodyFamilyDistributionLandSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyFamilyDistributionLand
        fields = ['id','name','createdBy']

class WaterBodyTankUniquenessSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyTankUniqueness
        fields = ['id','name','createdBy']

class WaterBodyBoundaryDropPointSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = WaterBodyBoundaryDropPoint
        fields = ['id','name','createdBy']




        


