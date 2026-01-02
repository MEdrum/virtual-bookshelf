from django.urls import path
from loan_request import views

urlpatterns = [
    path("", views.loan_requests_overview, name="loan_requests"),
]