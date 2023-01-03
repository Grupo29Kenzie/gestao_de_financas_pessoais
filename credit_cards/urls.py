from django.urls import path
from . import views

urlpatterns = [
    path("credit_cards/", views.CreditCardView),
]
