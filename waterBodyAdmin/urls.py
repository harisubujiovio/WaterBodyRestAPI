from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('roles',views.RoleViewSet)
router.register('userprofile',views.UserProfileViewSet)
router.register('allusers',views.UserList,basename='allusers')
router.register('tankImage',views.TankImageViewSet)
router.register('tankMetaData',views.TankMetaDataViewSet)
router.register('surveyQuestion',views.SurevyQuestionViewSet)

#URL Config Module
urlpatterns = router.urls