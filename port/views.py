from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Project
def name(request):
    context = {
        'linked_in':settings.LINKEDIN_URL,
        'github':settings.GITHUB_URL
    }
    return render(request,'home.html',context)

def project(request):
    context = {
        'linked_in':settings.LINKEDIN_URL,
        'github':settings.GITHUB_URL,
        'projects':Project.objects.all(),
    }
    return render(request,'project.html',context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject=f"New Contact Form Message from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['akshaysuresan02@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Your message has been sent successfully!")

    context = {
        'linked_in':settings.LINKEDIN_URL,
        'github':settings.GITHUB_URL
    }
    return render(request,'contact.html',context)

def about(request):
    context = {
        'linked_in':settings.LINKEDIN_URL,
        'github':settings.GITHUB_URL
    }
    return render(request,'about.html',context)