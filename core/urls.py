from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'))
]

router = DefaultRouter()
router.register('users',views.UserViewSet)
#URL Config Module
urlpatterns += router.urls
