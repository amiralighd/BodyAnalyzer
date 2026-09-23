from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from Analyzer.models import BodyAnalysis


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()

        return render(
            request,
            'accounts/register.html',
            {'form': form}
        )

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'You are registered and logged in now.'
            )

            return redirect('Home:home')

        return render(
            request,
            'accounts/register.html',
            {'form': form}
        )


class LoginView(View):

    def get(self, request):
        form = LoginForm()

        return render(
            request,
            'accounts/login.html',
            {'form': form}
        )

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                'You are logged in now.'
            )

            return redirect('Home:home')

        return render(
            request,
            'accounts/login.html',
            {'form': form}
        )


class LogoutView(View):

    def get(self, request):

        logout(request)

        return redirect('Home:home')


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):

        analyses = BodyAnalysis.objects.filter(
            user=request.user
        ).order_by('-created_at')

        return render(
            request,
            'accounts/dashboard.html',
            {
                'analyses': analyses
            }
        )