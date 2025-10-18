# bookproject/accounts/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm



class SignupView(CreateView):
    template_name = 'accounts/signup.html'

    form_class = SignupForm

    success_url = reverse_lazy('index')

    # GET でも
    # POST でも
    # model は参照されない
    # model = User