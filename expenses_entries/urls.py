from django.urls import path
from . import views

urlpatterns = [
    path("expenses_entries/", views.ExpenseEntrieView),
]
