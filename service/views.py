from django.shortcuts import render
from .models import Services , Facts
from django.views.generic import ListView
# Create your views here.


class ServicesListView(ListView):
    model = Services
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["facts"] = Facts.objects.last()
        return context
    

 