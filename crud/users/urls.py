from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users-list'),
    path('user/<int:pk>/', views.user_detail, name='user-detail'),
    path('user/<int:pk>/edit/', views.user_update, name='user-update'),
    path('user/<int:pk>/delete/', views.user_delete, name='user-delete'),
    path('user/add/', views.user_create, name='user-create'),
    path('user/<int:pk>/', views.user_detail, name='user-detail'),
]
