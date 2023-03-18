from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class RatsViewSet(viewsets.ModelViewSet):
    queryset = Rats.objects.all()
    serializer_class = RatsSerializer
    permission_classes = [IsAuthenticated]


class MouseTrapViewSet(viewsets.ModelViewSet):
    queryset = MouseTrap.objects.all()
    serializer_class = MouseTrapSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MouseTrap2ViewSet(viewsets.ModelViewSet):
    queryset = MouseTrap2.objects.all()
    serializer_class = MouseTrap2Serializer