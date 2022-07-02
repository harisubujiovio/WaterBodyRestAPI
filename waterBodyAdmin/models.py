from pickle import FALSE, TRUE
from django.conf import settings
from django.db import models
from uuid import uuid4

# Create your models here.
class CardSummaryData(models.Model):
    label = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    data = models.IntegerField()
    filterKey = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    class Meta:
     managed = False

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
    mobileNumber = models.CharField(max_length=20,blank=False,unique=TRUE)
    address = models.TextField()
    district = models.TextField(blank=TRUE)
    division = models.TextField(blank=TRUE)
    region = models.TextField(blank=TRUE)
    block = models.TextField(blank=TRUE)
    state = models.TextField(blank=TRUE)
    pincode = models.IntegerField(blank=FALSE)
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
    code = models.IntegerField(null=True,blank=True)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class District(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    code = models.IntegerField(null=True,blank=True)
    name = models.CharField(max_length=255)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class Block(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    code = models.IntegerField(null=True,blank=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,related_name='blocks')
    name = models.CharField(max_length=255)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def districtname(self):
        return self.district.name

class Panchayat(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    code = models.IntegerField(null=True,blank=True)
    block = models.ForeignKey(Block,on_delete=models.CASCADE,related_name='panchayats')
    name = models.CharField(max_length=255)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def blockname(self):
        return self.block.name

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

class WaterBodyBundIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySpreadIssues(models.Model):
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

class Section(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class SectionQuestion(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    section = models.ForeignKey(Section,on_delete=models.CASCADE, related_name='questions')
    name = models.CharField(max_length=255)
    fieldType = models.CharField(max_length=255)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("section", "name"),)

class WaterBodySectionType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    waterbodytype = models.ForeignKey(WaterBodyType,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("section", "waterbodytype"),)

class WaterBodyTankType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.TextField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyAvailability(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.TextField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyCatchmentType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.TextField(max_length=255,unique=True)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySurveyResponse(models.Model):
    uniqueid = models.UUIDField(primary_key=True)
    name = models.TextField()
    taluk = models.ForeignKey(Taluk,on_delete=models.CASCADE,related_name='taluk')
    block = models.ForeignKey(Block,on_delete=models.CASCADE,related_name='block')
    panchayat = models.ForeignKey(Panchayat,on_delete=models.CASCADE,related_name='panchayat')
    village = models.CharField(max_length=255)
    surveyno = models.TextField()
    waterbodytype = models.ForeignKey(WaterBodyType,on_delete=models.CASCADE,related_name='waterbodytype')
    ownership = models.ForeignKey(WaterBodyOwnerShip,on_delete=models.CASCADE,related_name='ownership')
    tanktype = models.ForeignKey(WaterBodyTankType,on_delete=models.CASCADE,related_name='tanktype')
    neerkattipractice = models.CharField(max_length=10)
    legalissue = models.BooleanField();
    status = models.CharField(max_length=100)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyHydrologicResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='HydrologicParameter')
    waterspreadArea = models.IntegerField()
    registeredAyacut = models.IntegerField()
    capacity = models.IntegerField()
    numberoffillings = models.IntegerField()
    firstmonthfilling = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='firstmonthfilling')
    waterAvailability = models.ForeignKey(WaterBodyAvailability,on_delete=models.CASCADE,related_name='waterAvailability')
    monthdryup = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='monthdryup')
    numberofsources = models.IntegerField()
    catchmentType = models.ForeignKey(WaterBodyCatchmentType,on_delete=models.CASCADE,related_name='catchmentType')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyHydrologicalSourceSupply(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    hydrologicalResponse = models.ForeignKey(WaterBodyHydrologicResponse,on_delete=models.CASCADE,related_name='Sources')
    source = models.ForeignKey(WaterBodySource,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyHydrologicalPrioritySourceSupply(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    hydrologicalResponse = models.ForeignKey(WaterBodyHydrologicResponse,on_delete=models.CASCADE,related_name='PrioritySources')
    prioritysource = models.ForeignKey(WaterBodySource,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySourceResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='SourceParameter')
    source1 = models.ForeignKey(WaterBodySource,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFreeCatchmentResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='FreeCatchment')
    sourcecontributiontype = models.CharField(max_length=255)
    contributiontypepercentage = models.IntegerField()
    seassonstart = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='FreeCatchmentSeassonStart')
    seassonend = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='FreeCatchmentSeassonEnd')
    streamtype = models.ForeignKey(WaterBodyCrossSection,on_delete=models.CASCADE)
    streamheadtopwidth = models.IntegerField(default=0)
    streamheadbed = models.IntegerField(default=0)
    streamheaddepth = models.IntegerField(default=0)
    streammiddletopwidth = models.IntegerField(default=0)
    streammiddlebed = models.IntegerField(default=0)
    streammiddledepth = models.IntegerField(default=0)
    streamtailendtopwidth = models.IntegerField(default=0)
    streamtailendbed = models.IntegerField(default=0)
    streamtailenddepth = models.IntegerField(default=0)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFreeCatchmentStreamIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    freeCatchmentResponse = models.ForeignKey(WaterBodyFreeCatchmentResponse,on_delete=models.CASCADE,related_name='Issues')
    issue = models.ForeignKey(WaterBodyStreamIssues,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySurPlusFromUpStreamResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='SurplusFromUpStream')
    tankName = models.CharField(max_length=255)
    sourcecontributiontype = models.CharField(max_length=255)
    contributiontypepercentage = models.IntegerField()
    seassonstart = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='surplusseassonstart')
    seassonend = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='surplusseassonend')
    streamtype = models.ForeignKey(WaterBodyCrossSection,on_delete=models.CASCADE)
    actualbreadth = models.IntegerField()
    currentbreadth = models.IntegerField()
    actualbottomwidth = models.IntegerField()
    currentbottomwidth = models.IntegerField()
    actualdepth = models.IntegerField()
    currentdepth = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyUpperTankSluiceResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='UpperTankSluice')
    tankName = models.CharField(max_length=255)
    contributionpercentage = models.IntegerField()
    seassonstart = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='UpperTankSluiceSeassonStart')
    seassonend = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='UpperTankSluiceSeassonEnd')
    streamtype = models.ForeignKey(WaterBodyCrossSection,on_delete=models.CASCADE)
    streamheadtopwidth = models.IntegerField(default=0)
    streamheadbed = models.IntegerField(default=0)
    streamheaddepth = models.IntegerField(default=0)
    streammiddletopwidth = models.IntegerField(default=0)
    streammiddlebed = models.IntegerField(default=0)
    streammiddledepth = models.IntegerField(default=0)
    streamtailendtopwidth = models.IntegerField(default=0)
    streamtailendbed = models.IntegerField(default=0)
    streamtailenddepth = models.IntegerField(default=0)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyUpperTankSluiceStreamIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    upperTankSluiceResponse = models.ForeignKey(WaterBodyUpperTankSluiceResponse,on_delete=models.CASCADE,related_name='Issues')
    issue = models.ForeignKey(WaterBodyStreamIssues,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyIrrigationCanalResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='IrigationCanal')
    canalName = models.CharField(max_length=255)
    bednature = models.CharField(max_length=255)
    numberofSupplies = models.IntegerField()
    firstseassonstart = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='IrrigationCanalfirstSeassonStart')
    firstseassonend = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='IrrigationCanalfirstSeassonEnd')
    secondseassonstart = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='IrrigationCanalsecondSeassonStart')
    secondseassonend = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='IrrigationCanalsecondSeassonEnd')
    contributiontypepercentage = models.IntegerField()
    streamtype = models.ForeignKey(WaterBodyCrossSection,on_delete=models.CASCADE)
    streamtopwidth = models.IntegerField()
    streambed = models.IntegerField()
    streamdepth = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyIrrigationCanalStreamIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    IrrigationCanalResponse = models.ForeignKey(WaterBodyIrrigationCanalResponse,on_delete=models.CASCADE,related_name='Issues')
    issue = models.ForeignKey(WaterBodyStreamIssues,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyRiverStreamResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='RiverStream')
    riverName = models.CharField(max_length=255)
    bednature = models.CharField(max_length=255)
    seassonstart = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='RiverStreamseassonStart')
    seassonend = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='RiverStreamseassonEnd')
    contributiontypepercentage = models.IntegerField()
    streamtype = models.ForeignKey(WaterBodyCrossSection,on_delete=models.CASCADE)
    streamtopwidth = models.IntegerField()
    streambed = models.IntegerField()
    streamdepth = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyRiverStreamIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    RiverStreamResponse = models.ForeignKey(WaterBodyRiverStreamResponse,on_delete=models.CASCADE,related_name='Issues')
    issue = models.ForeignKey(WaterBodyStreamIssues,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySpreadResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Spread')
    spreadpercentage = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySpreadAreaIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    spreadResponse = models.ForeignKey(WaterBodySpreadResponse,on_delete=models.CASCADE,related_name='SpreadAreaIssues')
    issue = models.ForeignKey(WaterBodySpreadIssues,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySpreadInvasiveSpecies(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    spreadResponse = models.ForeignKey(WaterBodySpreadResponse,on_delete=models.CASCADE,related_name='SpreadAreaSpecies')
    specie = models.ForeignKey(WaterBodyExoticSpecies,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)


class WaterBodyBundResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Bund')
    bundlength = models.IntegerField()
    bundtopwidth = models.IntegerField()
    slopefrontside = models.IntegerField()
    sloperearside = models.IntegerField()
    stonepitchingcondition = models.ForeignKey(WaterBodyStonePitchingCondition,on_delete=models.CASCADE,related_name='Stonepitchingconditions')
    revetmentlength = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyBundIssuesResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    bundResponse = models.ForeignKey(WaterBodyBundResponse,on_delete=models.CASCADE,related_name='BundIssues')
    issue = models.ForeignKey(WaterBodyBundIssues,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyBundFunctionalites(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    bundResponse = models.ForeignKey(WaterBodyBundResponse,on_delete=models.CASCADE,related_name='Functionalites')
    bundfunctionality = models.ForeignKey(WaterBodyBund,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyBundStonePitchings(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    bundResponse = models.ForeignKey(WaterBodyBundResponse,on_delete=models.CASCADE,related_name='Pitchings')
    stonePitching = models.ForeignKey(WaterBodyStonePitching,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)


class WaterBodySluiceResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Sluice')
    sluicenumber = models.IntegerField()
    sluicetype = models.ForeignKey(WaterBodySluice,on_delete=models.CASCADE,related_name='SluiceType')
    sluiceIrrigatedArea = models.IntegerField()
    silllevelDepth = models.ForeignKey(WaterBodyDepthSillLevel,on_delete=models.CASCADE,related_name='SluiceSillLevelDepth')
    shutterType = models.ForeignKey(WaterBodyShutter,on_delete=models.CASCADE,related_name='SluiceShutterType')
    sluicecondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='SluiceCondition')
    shuttercondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='ShutterCondition')
    sluicefeedanywaterbody =  models.CharField(max_length=10)
    waterbodyname =  models.CharField(max_length=255)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySurplusweirResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Surplusweir')
    surplusweirnumber = models.IntegerField()
    surplusweirtype = models.ForeignKey(WaterBodySurplusWeir,on_delete=models.CASCADE,related_name='Surplusweirtype')
    surplusweirLength = models.IntegerField()
    silllevelDepth = models.ForeignKey(WaterBodyDepthSillLevel,on_delete=models.CASCADE,related_name='SurplusweirSillLevelDepth')
    mwlstones = models.ForeignKey(WaterBodyMWLStone,on_delete=models.CASCADE,related_name='MWLStone')
    mwlstonedepth = models.IntegerField()
    leveldifference = models.IntegerField()
    shutterType = models.ForeignKey(WaterBodyShutter,on_delete=models.CASCADE,related_name='SurplusweirShutterType')
    surplusweircondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='Surplusweircondition')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySurpluCoarseResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='SurpluCoarse')
    tankName = models.CharField(max_length=255)
    streamtype = models.ForeignKey(WaterBodyCrossSection,on_delete=models.CASCADE)
    actualbreadth = models.IntegerField()
    currentbreadth = models.IntegerField()
    actualbottomwidth = models.IntegerField()
    currentbottomwidth = models.IntegerField()
    actualdepth = models.IntegerField()
    currentdepth = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodySurpluCoarseIssues(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surpluCoarseResponse = models.ForeignKey(WaterBodySurpluCoarseResponse,on_delete=models.CASCADE,related_name='Issues')
    issue = models.ForeignKey(WaterBodyStreamIssues,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyIrrigationResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Irrigation')
    ayacutcultivation = models.IntegerField()
    ayacutnature = models.ForeignKey(WaterBodyAyacutNonCultivation,on_delete=models.CASCADE)
    cropping = models.ForeignKey(WaterBodyCropping,on_delete=models.CASCADE)
    firstcropname = models.CharField(max_length=255)
    secondcropname = models.CharField(max_length=255)
    thirdcropname = models.CharField(max_length=255)
    dugwellnumber = models.IntegerField()
    depthofdugwell = models.IntegerField()
    borewellnumber = models.IntegerField()
    maxborewelldepth = models.IntegerField()
    dependentfamiliesnumber = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFishingResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Fishing')
    investmentnature = models.ForeignKey(WaterBodyInvestmentNature,on_delete=models.CASCADE,related_name='Investmentnature')
    monthofrelease = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='Monthofrelease')
    monthofharvest = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='Monthofharvest')
    investment = models.IntegerField()
    returns = models.IntegerField()
    dependentfamiliesnumber = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyLotusCultivationResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='LotusCultivation')
    investmentnature = models.ForeignKey(WaterBodyInvestmentNature,on_delete=models.CASCADE,related_name='LotusInvestmentnature')
    monthofrelease = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='LotusMonthofrelease')
    monthofharvest = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='LotusMonthofharvest')
    investment = models.IntegerField()
    returns = models.IntegerField()
    dependentfamiliesnumber = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyTankBedCultivationResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='TankBedCultivation')
    area = models.IntegerField()
    dependentfamiliesnumber = models.IntegerField()
    monthofrelease = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='TankBedMonthofrelease')
    monthofharvest = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='TankBedMonthofharvest')
    investment = models.IntegerField()
    returns = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyTankBedFamilies(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    tankBedResponse = models.ForeignKey(WaterBodyTankBedCultivationResponse,on_delete=models.CASCADE,related_name='Families')
    family = models.ForeignKey(WaterBodyFamilyNature,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyTankBedDistributionLands(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    tankBedResponse = models.ForeignKey(WaterBodyTankBedCultivationResponse,on_delete=models.CASCADE,related_name='DistributionLands')
    distributionLand = models.ForeignKey(WaterBodyFamilyDistributionLand,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyHarvestFromBundTreeResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='HarvestFromBundTree')
    investmentnature = models.ForeignKey(WaterBodyInvestmentNature,on_delete=models.CASCADE,related_name='BundTreeInvestmentnature')
    monthofrelease = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='HarvestFromBundMonthofrelease')
    monthofharvest = models.ForeignKey(Month,on_delete=models.CASCADE,related_name='HarvestFromBundMonthofharvest')
    investment = models.IntegerField()
    returns = models.IntegerField()
    dependentfamiliesnumber = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyForPotteryResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Pottery')
    dependentfamiliesnumber = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyForLiveStockResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='LiveStock')
    dependentfamiliesnumber = models.IntegerField()
    dependentanimalssnumber = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyTankUniquenessResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='TankUniqueness')
    name = models.ForeignKey(WaterBodyTankUniqueness,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFunctionalParameterResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='FunctionalParameters')
    tankFunction = models.ForeignKey(WaterBodyIrrigationTankFunction,on_delete=models.CASCADE)
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyInletResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Inlets')
    inletnumber = models.IntegerField()
    inlettype = models.ForeignKey(WaterBodyInletType,on_delete=models.CASCADE,related_name='InletType')
    inletcondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='InletCondition')
    slittrap = models.ForeignKey(WaterBodySlitTrap,on_delete=models.CASCADE,related_name='SlitTrap')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyOutletResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Outlets')
    outletnumber = models.IntegerField()
    outlettype = models.ForeignKey(WaterBodyOutletType,on_delete=models.CASCADE,related_name='InletType')
    outletcondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='OutletCondition')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyGhatsResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Ghats')
    ghatnumber = models.IntegerField()
    ghatcondition = models.ForeignKey(WaterBodyGhatCondition,on_delete=models.CASCADE,related_name='GhatCondition')
    numberofghatsneeded = models.IntegerField()
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyFencingResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Fencings')
    fencetype = models.ForeignKey(WaterBodyFenceType,on_delete=models.CASCADE,related_name='FenceType')
    fencecondition = models.ForeignKey(WaterBodyFenceCondition,on_delete=models.CASCADE,related_name='FenceCondition')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyDomesticResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Domestics')
    dependentfamiliesnumber = models.IntegerField()
    dependentlivestocksnumber = models.IntegerField()
    dugwellnumber = models.IntegerField()
    depthofdugwell = models.IntegerField()
    dugwellcondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='DugwellCondition')
    numberofborewells = models.IntegerField()
    depthofborewell = models.IntegerField()
    borewellcondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='BorewellCondition')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

class WaterBodyDrinkingResponse(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    surveyResponse = models.ForeignKey(WaterBodySurveyResponse,on_delete=models.CASCADE,related_name='Drinkings')
    dependentfamiliesnumber = models.IntegerField()
    dugwellnumber = models.IntegerField()
    depthofdugwell = models.IntegerField()
    dugwellcondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='DrinkingDugwellCondition')
    numberofborewells = models.IntegerField()
    depthofborewell = models.IntegerField()
    borewellcondition = models.ForeignKey(WaterBodySluiceCondition,on_delete=models.CASCADE,related_name='DrinkingBorewellCondition')
    createdBy = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedBy = models.CharField(max_length=255,blank=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)