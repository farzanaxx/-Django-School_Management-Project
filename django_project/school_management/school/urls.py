
from . import views
from django.urls import path, include



urlpatterns = [
    path("", views.school_list, name="school_list"),
    path('create', views.scl_info, name="scl_info"),
    path('<int:id>/update', views.scl_update, name="scl_details"),
    path('<int:id>/delete', views.scl_delete, name="scl_delete"),
]