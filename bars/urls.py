from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='bars'),
    path('<int:bar_id>', views.bar, name='bar'),
    path('search', views.search, name='search')
]