from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
  if request.method == 'POST':
    form  = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created! You can login using the new account')
      return redirect('login')
  else:
    form= UserRegisterForm()
  return render(request, 'user/register.html',{'form': form})

@login_required
def profile(request):
  return render(request, 'user/profile.html')