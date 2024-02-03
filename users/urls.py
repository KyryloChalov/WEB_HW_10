from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('registration/', views.RegistrationPageView.as_view(), name='registration'),
    path('logout/', views.logoutuser, name='logout')
]
