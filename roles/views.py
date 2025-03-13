from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Role
from .forms import RoleForm

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin)
def role_list(request):
    roles = Role.objects.all()  # Fetch all roles from the database
    return render(request, 'role_list.html', {'roles': roles})

@user_passes_test(is_admin)
def add_role(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'add_role.html', {'form': form})

@user_passes_test(is_admin)
def update_role(request, role_id):
    role = get_object_or_404(Role, role_id=role_id)
    if request.method == "POST":
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'update_role.html', {'form': form})

@user_passes_test(is_admin)
def delete_role(request, role_id):
    role = get_object_or_404(Role, role_id=role_id)
    role.delete()
    return redirect('role_list')

# Non-admin view for public access (optional)
def role_list_public(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})