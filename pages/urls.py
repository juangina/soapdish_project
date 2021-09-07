from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('views/list', views.BarListView.as_view(), name='bar_list_view'),
    path('views/list/<str:creator>', views.CreatorBarListView.as_view(), name='creator_bar_list_view'),
    path('views/detail/<int:pk>', views.BarDetailView.as_view(), name='bar_detail.view')
]