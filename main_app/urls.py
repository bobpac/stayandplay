from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:pk>/delete_service', views.ServiceDelete.as_view(), name='services_delete'),
    path('dogs/<int:dog_id>/add_service', views.add_service, name='add_service'),
    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),
    path('dogs/<int:dog_id>/del_photo/', views.del_photo, name='del_photo'),
    path('dogs/<int:pk>/update_service/', views.ServiceUpdate.as_view(), name='services_update'),
    path('searchbar/', views.searchbar, name='searchbar'),
]
