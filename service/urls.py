from .views import ServicesListView

from django.urls import path 


app_name = "service"

urlpatterns = [
    path("",ServicesListView.as_view(),name="services_list"),
    
]

