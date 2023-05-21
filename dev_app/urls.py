from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dev_dashboard'),
    path('upload', views.DocumentCreateView.as_view(), name='document_upload')
]