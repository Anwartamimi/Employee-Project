from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'employee_app/home.html', {})

def dashboard(request):
    
    return render(request, 'employee_app/dashboard.html', {})

def analytics(request):
    
    return render(request, 'employee_app/analytics.html', {})

def messages(request):
    
    return render(request, 'employee_app/messages.html', {})

def collections(request):
    
    return render(request, 'employee_app/collections.html', {})

def users(request):
    
    return render(request, 'employee_app/users.html', {})

def settings(request):
    
    return render(request, 'employee_app/settings.html', {})

def notifications(request):
    
    return render(request, 'employee_app/notifications.html', {})