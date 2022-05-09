from django.conf import settings
from django.db import models
from uuid import uuid4

# Create your models here.

class Role(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=255)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    mobileNumber = models.CharField(max_length=20,blank=False)
    phoneNumber = models.CharField(max_length=20,null=True,blank=True)
    address = models.TextField()
    role = models.ForeignKey(Role,on_delete=models.PROTECT,blank=True,null=True,related_name='users')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def username(self):
        return self.user.username

    class Meta:
        ordering = ['user__first_name', 'user__last_name' ]

class TankImage(models.Model):
   image = models.FileField(upload_to='tanksinmadurai/files')
   createdBy = models.CharField(max_length=255)
   createdDate = models.DateTimeField(auto_now_add=True)

class TankMetaData(models.Model):
    Unique_id = models.CharField(max_length=255,primary_key=True)
    tankId = models.ForeignKey(TankImage,on_delete=models.PROTECT,blank=True,null=True,related_name='images')
    FID = models.CharField(max_length=255)
    CLUSTER = models.CharField(max_length=255)
    TANK_NUM = models.CharField(max_length=255)
    Tank_Name = models.CharField(max_length=255)
    Latitude = models.CharField(max_length=255)
    Longitude = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    Block = models.CharField(max_length=255)
    Taluk = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    Subbasin = models.CharField(max_length=255)
    Basin = models.CharField(max_length=255)
    Section = models.CharField(max_length=255)
    Sub_Dn = models.CharField(max_length=255)
    Division = models.CharField(max_length=255)
    Circle = models.CharField(max_length=255)
    Region = models.CharField(max_length=255)
    Tank_Type = models.CharField(max_length=255)
    Cap_MCM = models.CharField(max_length=255)
    FTL_m = models.CharField(max_length=255)
    MWL_m = models.CharField(max_length=255)
    TBL_m = models.CharField(max_length=255)
    Sto_Dep_m = models.CharField(max_length=255)
    Ayacut_ha = models.CharField(max_length=255)
    Catch_sqkm = models.CharField(max_length=255)
    Wat_Spr_ha = models.CharField(max_length=255)
    No_of_Weir = models.CharField(max_length=255)
    Weir_Len_m = models.CharField(max_length=255)
    No_Sluice = models.CharField(max_length=255)
    Low_Sil_m = models.CharField(max_length=255)
    Bund_Len_m = models.CharField(max_length=255)
    Dis_cusec = models.CharField(max_length=255)

class SurveyQuestionMetaData(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    question = models.TextField()
    status = models.BooleanField(default=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class TankSurveyQuestionResponse(models.Model):
    name = models.CharField(max_length=255)
    question = models.ForeignKey(SurveyQuestionMetaData,on_delete=models.CASCADE)
    responseText =  models.TextField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class Taluk(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class Block(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class Panchayat(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    blockId = models.ForeignKey(Block,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyOwnerShip(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySource(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyCrossSection(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyStreamIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyExoticSpecies(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyBund(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyTankIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyStonePitching(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyStonePitchingCondition(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySluice(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyDepthSillLevel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyShutter(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySluiceCondition(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyShutterCondition(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySurplusWeir(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyMWLStone(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyIrrigationTankFunction(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyAyacutNonCultivation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyCropping(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyInvestmentNature(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFamilyNature(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFamilyDistributionLand(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyTankUniqueness(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyBoundaryDropPoint(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyTempleTankType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyInletType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySlitTrap(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyOutletType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyGhatCondition(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFenceCondition(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFenceType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyOoraniFunction(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)


class Month(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

