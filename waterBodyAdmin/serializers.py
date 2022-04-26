import os
from rest_framework import serializers
from .models import SurveyQuestionMetaData, TankImage, TankMetaData, UserProfile
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

