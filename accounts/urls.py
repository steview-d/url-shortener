from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register
from accounts import urls_pw_reset

urlpatterns = [
    # user auth functionality
    path('login/', auth_views.LoginView.as_view(
        template_name="accounts/login.html",
        redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='index'), name="logout"),
    path('register/', register, name="register"),
    # password reset urls
    path('', include(urls_pw_reset)),
]
