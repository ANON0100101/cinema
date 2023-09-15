from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.cinema.views import *

router = DefaultRouter()
router.register('', MovieApiView)

urlpatterns = [


]
urlpatterns += router.urls
