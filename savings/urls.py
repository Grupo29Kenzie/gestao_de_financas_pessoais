from django.urls import path
from . import views

urlpatterns = [
    path("savings/", views.SavingView),
]
