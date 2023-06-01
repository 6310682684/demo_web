from django.urls import path
from . import views

urlpatterns = [
    path("person/create/", views.person_create, name = "person_create"),
    path("person/read/", views.person_read, name = "person_read"),
    path("person/update/<int:id>", views.person_update, name = "person_update"),
    path("person/delete/<int:id>" ,views.person_delete, name = "person_delete"),
]
