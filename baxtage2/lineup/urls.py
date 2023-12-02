from django.urls import path
from . import views
from django.urls import path
from .views import PerformanceCreateView, PerformanceListView, PerformanceDetailView

#
# urlpatterns = [
#     path('<slug:slug>', views.performance_detail, name='performance_detail'),
#     path('', views.performance_all, name='performance_all'),
#
# ]

app_name = 'lineup'

urlpatterns = [
    path('', PerformanceListView.as_view(), name='performance_list'),
    path('new', PerformanceCreateView.as_view(), name='performance_new'),
    path('<slug:slug>/', PerformanceDetailView.as_view(), name='performance_detail'),
]