from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'mousetrap', MouseTrapViewSet)
router.register(r'mousetrap2', MouseTrap2ViewSet)

urlpatterns = [
    path('API/', include(router.urls)),
]