from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .forms import UserForm

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def users_list(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user, edit=True)  # Pass edit=True here
        if form.is_valid():
            form.save()
            return redirect('users-list')  # Automatically redirect after save
    else:
        form = UserForm(instance=user, edit=True)  # Pass edit=True here

    return render(request, 'users/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users-list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})