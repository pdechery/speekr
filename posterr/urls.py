from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('profile/<int:user>', profile),
    path('users/', UserList.as_view(), name="user-list"),
    path('user/<int:user>/follow/<int:friend>', follow),
    path('user/<int:user>/unfollow/<int:friend>', unfollow),
    path('user/<int:pk>', UserDetail.as_view(), name="user-detail"),
    path('posts/', PostListCreate.as_view()),
]