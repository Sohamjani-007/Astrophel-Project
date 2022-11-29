from . import views
from .views import login
from django.urls import path

urlpatterns = [
    
    path('login/', login),
    path('paisa_to_rupee/', views.RupeeConvertionView.as_view()),
]


