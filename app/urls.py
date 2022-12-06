from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('social',SocialViewset)
router.register('profile',ProfileViewset)
router.register('portfolio',PortfolioViewset)
router.register('info',InfoViewset)
router.register('xabar',XabarViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('visitors',MyVisitors.as_view())
]
