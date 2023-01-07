from django.urls import path
from . import views

urlpatterns = [
    path("savings/", views.SavingView.as_view()),
    path("savings/<int:saving_id>", views.SavingDetailView.as_view()),
]
