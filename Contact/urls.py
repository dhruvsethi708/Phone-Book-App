from django.contrib import admin
from django.urls import path, include
from Contact import views, urls

urlpatterns = [
    path('', views.home),
    path('addcontact/', views.addcontact),
    path('allcontacts/', views.getAllContacts),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('searchcontact/', views.searchContact),

]


