# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.MouseTrap import views

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("MouseTrap/", include("apps.MouseTrap.urls")),             # UI Kits Html files
    path("SMALLS/", include("apps.SMALLS.urls")),             # UI Kits Html files
    path("", include("apps.home.urls"))             # UI Kits Html files
]
