from django.urls import path

from . import views

# Set the application namespace
app_name = "rpimanager"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:switch_id>/', views.switch_details, name='switch_details')
]