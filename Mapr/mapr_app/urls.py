from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vue/", views.vue_index, name="vue_index"),
    path("login/", views.login, name="login"),
    path("api/users", views.get_users, name="get_users"),
    path("api/groups", views.get_groups, name="get_groups"),
    path("api/groups/<int:group_id>", views.get_group_by_id, name="get_group_by_id"),
]
