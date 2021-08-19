from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class LandingPageView(View):
    def get(self,request):
        return render(request, 'index.html')


class AddDonationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
