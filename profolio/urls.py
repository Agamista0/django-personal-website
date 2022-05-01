from django.urls import path  
from .views import ProfolioList

app_name ="profolio"
urlpatterns = [
    path("",ProfolioList.as_view(),name="profolio_list")
]
