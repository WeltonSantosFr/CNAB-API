from django.urls import path, include
from .views import CNABViewSet, CNABDataViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cnab', CNABViewSet)
router.register(r'list', CNABDataViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.search)
]