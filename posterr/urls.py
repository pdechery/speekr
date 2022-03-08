from django.urls import path
from posterr import views

urlpatterns = [
    path('', views.home),
    path('profile/<int:user>', views.profile),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('user/<int:pk>', views.UserDetail.as_view(), name="user-detail"),
    path('posts/', views.PostList.as_view()),
]