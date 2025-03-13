from django.contrib import admin
from django.urls import path
from roles.views import role_list, add_role, update_role, delete_role

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', role_list, name='role_list'),
    path('roles/add/', add_role, name='add_role'),
    path('roles/update/<int:role_id>/', update_role, name='update_role'),
    path('roles/delete/<int:role_id>/', delete_role, name='delete_role'),
]