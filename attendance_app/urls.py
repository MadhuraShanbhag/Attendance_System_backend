from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'attendance_app'

urlpatterns = [
    path('login/', views.login_user_teacher, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home_dashboard/', views.Dash.as_view(), name='dash'),
]
