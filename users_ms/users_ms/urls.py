from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users_ms.views.user_view import  UserList
from users_ms.views.user_view import UserDetail
from users_ms.views.user_view import UserValidacion

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('users/<str:name>/<str:password>', UserValidacion.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)