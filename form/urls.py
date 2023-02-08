from django.urls import path, include
from .views import CNABViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cnab', CNABViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('data/', views.store_data_view, name='store_data'),
    path('form/', views.store_form_view, name='store_form')
]