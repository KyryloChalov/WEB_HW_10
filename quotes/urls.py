from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('tag/<int:pk>', views.TagPageView.as_view(), name='tag'),
    path('quote/create', login_required(views.CreateQuoteView.as_view()), name='create.quote')
]
