from django.urls import path
from . import views

app_name="person"

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('<int:id_person>/update/', views.update, name="update"),
    path('<int:id_person>/delete/', views.delete, name="delete"),
]