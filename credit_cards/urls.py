from django.urls import path
from . import views

urlpatterns = [
    path("credit_cards/", views.CreditCardView.as_view()),
    path("credit_cards/<int:pk>/", views.CreditCardDetailView.as_view()),
]
