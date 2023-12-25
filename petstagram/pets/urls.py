from django.urls import path

from petstagram.pets import views

urlpatterns = [
    path('', views.pet_all, name='list pets'),
    path('details/<int:pk>', views.pet_detail, name='pet details'),
    path('like/<int:pk>', views.like_pet, name='like pet'),
    path('create/', views.create_pet, name="create pet"),
    path('edit/<int:pk>', views.edit_pet, name='edit pet'),
    path('delete/<int:pk>', views.delete_pet, name='delete pet'),
    path('comment/<int:pk>', views.comment_pet, name='comment pet'),
]
