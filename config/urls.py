from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("user/", views.user_detail, name="user_detail"),
    path("join/", views.join_school, name="join_school"),
    path("school/<int:school_id>/", views.school_detail, name="school_detail"),
]
