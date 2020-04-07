from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/',views.create_user),
    path('create_task/',views.create_task),
    path('create_advice/',views.create_advice),
    path('edit_user/<int:id>/',views.edit_user),
    path('edit_advice/<int:id>/',views.edit_advice),
    path('edit_task/<int:id>/',views.edit_task),
    path('delete_task/<int:id>/',views.delete_task),
    path('delete_advice/<int:id>/',views.delete_advice),
]