from posixpath import basename
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('roles',views.RoleViewSet)
router.register('taluks',views.TalukViewSet)
router.register('districts',views.DistrictViewSet)
router.register('blocks',views.BlockViewSet)
router.register('panchayats',views.PanchayatViewSet)
router.register('waterbodytypes',views.WaterBodyTypeViewSet)
router.register('waterbodyownerships',views.WaterBodyOwnerShipViewSet)
router.register('months',views.MonthViewSet)
router.register('waterbodysources',views.WaterBodySourceViewSet)
router.register('waterbodycrosssections',views.WaterBodyCrossSectionViewSet)
router.register('waterbodystreamissues',views.WaterBodyStreamIssuesViewSet)
router.register('waterbodyexoticspecies',views.WaterBodyExoticSpeciesViewSet)
router.register('waterbodybunds',views.WaterBodyBundViewSet)
router.register('waterbodytankissues',views.WaterBodyTankIssuesViewSet)
router.register('waterbodystonepitchings',views.WaterBodyStonePitchingViewSet)
router.register('waterbodystonepitchingconditions',views.WaterBodyStonePitchingConditionViewSet)
router.register('waterbodysluices',views.WaterBodySluiceViewSet)
router.register('waterbodydepthsilllevels',views.WaterBodyDepthSillLevelViewSet)
router.register('waterbodyshutters',views.WaterBodyShutterViewSet)
router.register('waterbodyconditions',views.WaterBodyConditionViewSet)
router.register('waterbodyshutterconditions',views.WaterBodyShutterConditionViewSet)
router.register('waterbodysurplusweirs',views.WaterBodySurplusWeirViewSet)
router.register('waterbodymwlstones',views.WaterBodyMWLStoneViewSet)
router.register('waterbodyirrigationtankfunctions',views.WaterBodyIrrigationTankFunctionViewSet)
router.register('waterbodyayacutnoncultivations',views.WaterBodyAyacutNonCultivationViewSet)
router.register('waterbodycroppings',views.WaterBodyCroppingViewSet)
router.register('waterbodynatureinvestments',views.WaterBodyInvestmentNatureViewSet)
router.register('waterbodyfamilynatures',views.WaterBodyFamilyNatureViewSet)
router.register('waterbodyfamilydistributionlands',views.WaterBodyFamilyDistributionLandViewSet)
router.register('waterbodytankuniqueness',views.WaterBodyTankUniquenessViewSet)
router.register('waterbodyboundarydroppoints',views.WaterBodyBoundaryDropPointViewSet)
router.register('waterbodytypes',views.WaterBodyTypeViewSet)
router.register('waterbodytempletanktypes',views.WaterBodyTempleTankTypeViewSet)
router.register('waterbodyinlettypes',views.WaterBodyInletTypeViewSet)
router.register('waterbodyslittraps',views.WaterBodySlitTrapViewSet)
router.register('waterbodyoutlettypes',views.WaterBodyOutletTypeViewSet)
router.register('waterbodyghatconditions',views.WaterBodyGhatConditionViewSet)
router.register('waterbodyfenceconditions',views.WaterBodyFenceConditionViewSet)
router.register('waterbodyfencetypes',views.WaterBodyFenceTypeViewSet)
router.register('waterbodyooranifunctions',views.WaterBodyOoraniFunctionViewSet)
router.register('sections',views.SectionViewSet)
router.register('sectionquestions',views.SectionQuestionViewSet, basename='sectionquestion')
router.register('waterbodytypesections',views.WaterbodyTypeSectionViewSet, basename='waterbodytypesection')
router.register('waterbodysurveyresponse',views.WaterBodySurveyResponseViewSet)
router.register('waterbodyhydrologicresponse',views.WaterBodyHydrologicResponseViewSet,basename='hydrologic')
router.register('waterbodyhydrologicresponse',views.WaterBodySupplySource1ResponseViewSet,basename='Source1')
router.register('waterbodysupplysource1response',views.WaterBodySupplySource1ResponseViewSet,basename='source')
router.register('waterbodyfreecatchmentresponse',views.WaterBodyFreeCatchmentResponseViewSet,basename='freecatchment')
router.register('waterbodyirrigationcanalresponse',views.WaterBodyIrrigationCanalResponseViewSet,basename='irrigationcanal')
router.register('waterbodyspreadresponse',views.WaterBodySpreadResponseViewSet,basename='spreadresponse')
router.register('waterbodybundresponse',views.WaterBodyBundResponseViewSet,basename='bundresponse')
router.register('waterbodysluiceresponse',views.WaterBodySluiceResponseViewSet,basename='sluiceresponse')
router.register('waterbodysurplusweirresponse',views.WaterBodySurplusweirResponseViewSet,basename='surplusweirresponse')
router.register('waterbodysurpluCoarseresponse',views.WaterBodySurpluCoarseResponseViewSet,basename='surpluCoarseresponse')
router.register('waterbodyirrigationresponse',views.WaterBodyIrrigationResponseViewSet,basename='irrigationresponse')
router.register('waterbodyfishingresponse',views.WaterBodyFishingResponseViewSet,basename='fishingresponse')
router.register('waterbodylotuscultivationresponse',views.WaterBodyLotusCultivationResponseViewSet,basename='lotuscultivationresponse')
router.register('waterbodytankbedcultivationresponse',views.WaterBodyTankBedCultivationResponseViewSet,basename='tankbedcultivationresponse')
router.register('waterbodyharvestfrombundtreeresponse',views.WaterBodyHarvestFromBundTreeResponseViewSet,basename='harvestfrombundtree')
router.register('waterbodypotteryresponse',views.WaterBodyForPotteryResponseViewSet,basename='pottery')
router.register('waterbodylivestockresponse',views.WaterBodyForLiveStockResponseViewSet,basename='livestockresponse')
router.register('waterbodyinletresponse',views.WaterBodyInletResponseSerializerViewSet,basename='inletresponse')
router.register('waterbodyoutletresponse',views.WaterBodyOutletResponseSerializerViewSet,basename='outletresponse')
router.register('waterbodyghatresponse',views.WaterBodyGhatsResponseSerializerViewSet,basename='ghatresponse')
router.register('waterbodyfencingresponse',views.WaterBodyFencingResponseSerializerViewSet,basename='fencingresponse')
router.register('waterbodydomesticresponse',views.WaterBodyDomesticResponseSerializerViewSet,basename='domesticresponse')
router.register('waterbodydrinkingresponse',views.WaterBodyDrinkingResponseSerializerViewSet,basename='drinkingresponse')
router.register('userprofile',views.UserProfileViewSet)
router.register('allusers',views.UserList,basename='allusers')
router.register('tankImage',views.TankImageViewSet)
router.register('tankMetaData',views.TankMetaDataViewSet)
router.register('surveyQuestion',views.SurevyQuestionViewSet)
router.register('waterBodyTankType',views.WaterBodyTankTypeViewSet)
router.register('waterBodyBedNature',views.WaterBodyBedNatureViewSet)
router.register('waterBodyAvailability',views.WaterBodyAvailabilityViewSet)
router.register('waterBodyCatchmentType',views.WaterBodyCatchmentTypeViewSet)
router.register('waterBodyBundIssues',views.WaterBodyBundIssuesViewSet)
router.register('waterBodySpreadIssues',views.WaterBodySpreadIssuesViewSet)
router.register('waterBodyBarrelType',views.WaterBodyBarrelTypeViewSet)
router.register('waterBodyFieldChannelType',views.WaterBodyFieldChannelTypeViewSet)
router.register('waterbodyirrigationcanalresponse',views.WaterBodyIrrigationCanalResponseViewSet,basename='irrigationcanalresponse')
router.register('waterbodyriverstreamresponse',views.WaterBodyRiverStreamResponseViewSet,basename='riverStreamresponse')
router.register('waterbodyuppertanksluiceresponse',views.WaterBodyUpperTankSluiceResponseViewSet,basename='uppertanksluiceresponse')
router.register('waterBodysurplussluiceUppertankresponse',views.WaterBodySurPlusSluiceUpperTankResponseViewSet,basename='uppertanksurplussluiceresponse')
router.register('waterbodyspringresponse',views.WaterBodySpringResponseViewSet,basename='springresponse')
router.register('waterbodysubsurfaceresponse',views.WaterBodySubSurfaceResponseViewSet,basename='subsurfaceresponse')
router.register('waterbodyPermissionType',views.PermissionTypeViewSet)
router.register('waterbodyPermissionType',views.PermissionTypeViewSet)
router.register('waterbodyResourceType',views.ResourceTypeViewSet)
router.register('waterbodyAccessRights',views.AccessRightsViewSet)
router.register('waterbodyResourcePermission',views.ResourcePermissionViewSet)
#URL Config Module
urlpatterns = router.urls