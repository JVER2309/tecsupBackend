from django.urls import path

from . import views

urlpatterns = [
    path('usuario',views.UserCreateView.as_view()),
]