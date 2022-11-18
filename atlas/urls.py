from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^paisa_to_rupee/$', views.RupeeConvertionView.as_view(), name='atlas_money'),
]



