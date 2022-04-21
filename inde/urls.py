from django.urls import path
from . import views



urlpatterns = [
    path('',views.inde, name="inde"),
]
