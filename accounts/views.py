from django.shortcuts import redirect, render
from .models import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    formContext = {
        'form':form
    }
    return render(request, 'register.html', formContext)