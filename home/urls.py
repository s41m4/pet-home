from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from home import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.default_map, name="default"),
    path('', views.index, name='index'),
    #path('', index(), name='index'),
]