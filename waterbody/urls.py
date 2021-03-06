"""waterbody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from waterBodyAdmin.views import AccessRightsViewSet, UserProfileViewSet,CardSummaryView,AddressView

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('waterBodyAdmin/', include('waterBodyAdmin.urls')),
    path('core/', include('core.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('waterBodyAdmin/cardsummary/', CardSummaryView.as_view()),
    path('waterBodyAdmin/address/', AddressView.as_view()),
    # path('password/reset/<str:uid>/<str:token>/',reset_user_password),
    # path('password/reset/<str:uid>/<str:token>/',reset_user_password),
    path('waterBodyAdmin/userprofile/<pk>/user/<int:user_id>/', UserProfileViewSet.as_view({"delete": "deleteUser"})),
    path('waterBodyAdmin/userprofile/<pk>/updateuser/<int:user_id>/', UserProfileViewSet.as_view({"patch": "updateUser"})),
    path('waterBodyAdmin/AccessRights/getRolePermissions/<role_id>/', AccessRightsViewSet.as_view({"get": "getRolePermissions"})),
    path('waterBodyAdmin/AccessRights/getResourcePermission/<role_id>/<resource_name>/<permission_name>', AccessRightsViewSet.as_view({"get": "getResourcePermission"})),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)