from django.shortcuts import render
from .pagination import MyPagination
# Create your views here.
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
class SocialViewset(ModelViewSet):
    queryset = SocialLinks.objects.all().order_by('-id')[:1]
    serializer_class = SocialLinksSerializer
class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all().order_by('-id')[:1]
    serializer_class = ProfileSerializer
class XabarViewset(ModelViewSet):
    queryset = Xabarlar.objects.all()
    serializer_class = XabarlarSerializer
class PortfolioViewset(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    pagination_class = MyPagination
class InfoViewset(ModelViewSet):
    queryset = Info.objects.all().order_by('-id')[:1]
    serializer_class = InfoSerializer