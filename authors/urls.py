from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'authors'

urlpatterns = [
    path('author/<int:pk>', views.AuthorPageView.as_view(), name='details'),
    path('create/', login_required(views.CreateAuthorView.as_view()), name='create.author')
]
