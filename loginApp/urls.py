from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from loginApp import views

urlpatterns = [
    path('profile/', views.LoginView.as_view()),
    path('api/auth/', views.CustomAuthToken.as_view()),
    path('register/',views.register.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)