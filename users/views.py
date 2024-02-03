from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpRequest
from braces.views import AnonymousRequiredMixin
from .forms import LoginForm, RegistrationForm


# Create your views here.
class LoginPageView(AnonymousRequiredMixin, View):
    template_name = "users/login.html"

    def get(self, request: HttpRequest):
        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request: HttpRequest):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes:main')


class RegistrationPageView(AnonymousRequiredMixin, View):
    template_name = "users/registration.html"

    def get(self, request: HttpRequest):
        return render(request, self.template_name, {'form': RegistrationForm})

    def post(self, request: HttpRequest):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect(to='quotes:main')
        else:
            return render(request, 'users/registration.html', {'form': form})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:main')
