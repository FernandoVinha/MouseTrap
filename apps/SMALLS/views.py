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

class SMALLSViewSet(viewsets.ModelViewSet):
    queryset = SMALLS.objects.all()
    serializer_class = SMALLSSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)