from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from home import views


urlpatterns = [
    path('users/', views.users, name='users'),
    path('announcement/', views.announcement, name='announcement'),
    path('add_announcement/', views.add_announcement, name='add_announcement'),
    path('user_profile', views.user_profile, name="user_profile"),
    path('update_user/', views.updateUser, name='update_user'),
    path('delete_user/<str:pk>/', views.deleteUser, name='delete_user'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.default_map, name="default"),
    path('', views.index, name='index'),
    #path('', index(), name='index'),
]