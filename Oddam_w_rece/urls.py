from django.contrib import admin
from django.urls import path
from oddam_w_dobre_rece import views as ex_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ex_views.LandingPageView.as_view(), name='landing'),
    path('add/', ex_views.AddDonationView.as_view(), name='add_donation'),
    path('login/', ex_views.LoginView.as_view(), name='login'),
    path('register/', ex_views.RegisterView.as_view(), name='register'),
]
