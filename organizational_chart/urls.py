from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizational_chart_view, name='organizational_chart'),
    path('json/', views.organizational_chart_json, name='organizational_chart_json'),
]