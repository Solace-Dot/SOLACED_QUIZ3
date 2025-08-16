from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("jobs:job_list")  # Redirect to jobs main page
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def profile(request):
    return render(request, "accounts/profile.html")