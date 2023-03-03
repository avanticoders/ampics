from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signin/', views.signin, name="signin"),
    path('user-profile/', views.user_profile, name="user-profile"),
    path('upload/', views.upload, name="upload"),
    path('search/', views.search_images, name="search/"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="password-reset.html"), name="reset_password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="password-reset-done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), name="password_reset_complete")
]