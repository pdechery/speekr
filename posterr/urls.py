from django.urls import path, include
from .views import *

rest_api = [
    path('home/', home),
    path('profile/<int:user>', profile),
    path('users/', UserList.as_view(), name="user-list"),
    path('user/<int:user>/follow/<int:friend>', follow),
    path('user/<int:user>/unfollow/<int:friend>', unfollow),
    path('user/<int:pk>', UserDetail.as_view(), name="user-detail"),
    path('posts/', PostCreate.as_view()),
    path('repost/', RepostCreate.as_view()),
    path('quote/', QuoteCreate.as_view()),
]

urlpatterns = [
    path('', HomePage),
    path('profile/<int:user>', Profile),
    path('api/', include(rest_api))
]