from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('penguins/', views.penguins_index, name='index'),
    path('penguins/<int:penguin_id>/', views.penguins_detail, name='detail'),
    path('penguins/create/', views.PenguinCreate.as_view(), name='penguins_create'),
    path('penguins/<int:pk>/update/', views.PenguinUpdate.as_view(), name='penguins_update'),
    path('penguins/<int:pk>/delete/', views.PenguinDelete.as_view(), name='penguins_delete'),
    path('penguins/<int:penguin_id>/add_swimming/', views.add_swimming, name='add_swimming'),
    path('penguins/<int:penguin_id>/assoc_clothes/<int:clothes_id>/', views.assoc_clothes, name='assoc_clothes'),
    path('penguins/<int:penguin_id>/unassoc_clothes/<int:clothes_id>/', views.unassoc_clothes, name='unassoc_clothes'),
    path('clothes/', views.ClothesList.as_view(), name='clothes_index'),
    path('clothes/<int:pk>/', views.ClothesDetail.as_view(), name='clothes_detail'),
    path('clothes/create/', views.ClothesCreate.as_view(), name='clothes_create'),
    path('clothes/<int:pk>/update/', views.ClothesUpdate.as_view(), name='clothes_update'),
    path('clothes/<int:pk>/delete/', views.ClothesDelete.as_view(), name='clothes_delete'),
    path('penguins/<int:penguin_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]