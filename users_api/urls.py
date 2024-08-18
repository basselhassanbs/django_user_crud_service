from django.urls import path

from . import views

urlpatterns = [
    path("api/users", views.UserApiView.as_view()),
    path("api/users/<int:id>", views.UserDetailApiView.as_view()),
]