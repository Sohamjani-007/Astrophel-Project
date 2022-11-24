from . import views
from django.urls import path

urlpatterns = [
    path('paisa_to_rupee/', views.RupeeConvertionView.as_view()),
]


