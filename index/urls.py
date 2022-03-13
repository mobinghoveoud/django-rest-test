from django.urls import include, path
from index.views import UserList, UserDetail, UserLogin, UserVerify, UserLogout

app_name = "index"

urlpatterns = [
    # Users
    path('users/', UserList.as_view(), name='list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='detail'),

    # Auth
    path('auth/login/', UserLogin.as_view(), name='login'),
    path('auth/verify/<str:code>/', UserVerify.as_view(), name='verify'),
    path('auth/logout/', UserLogout.as_view(), name='logout'),
]
