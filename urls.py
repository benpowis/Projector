from django.urls import path, include

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('insight/', views.InsightView.as_view(), name='insight'),
]
