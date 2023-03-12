from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views


router = routers.DefaultRouter()
router.register(r'SMALLS', SMALLSViewSet)

urlpatterns = [
    path('API/', include(router.urls)),
]