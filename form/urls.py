from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("process_cnab", views.process_cnab, name="process_cnab")
]