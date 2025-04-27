from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import CustomLoginView, SignUpView

urlpatterns =  [
    path('login/', CustomLoginView.as_view(), name = 'login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page = '/'), name = 'logout'), 
    path('sign_up/', SignUpView.as_view() , name = 'signup'),
]