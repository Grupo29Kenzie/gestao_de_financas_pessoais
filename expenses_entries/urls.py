from django.urls import path
from . import views

urlpatterns = [
    path("expenses_entries/", views.ExpenseEntrieView.as_view()),
    path("expenses_entries/<int:pk>/", views.ExpenseEntrieDetailView.as_view()),
]
