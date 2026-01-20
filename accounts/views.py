from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    """
    Displays the signup form
    Handles user registrations
    The user is logged in automatically after account creation
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response