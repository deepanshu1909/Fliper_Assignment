from django.shortcuts import render, redirect
from .models import Project, Client, ContactFormSubmission, NewsletterSubscription
from django.contrib import messages

def landing_page(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    return render(request, 'landing/landing_page.html', {'projects': projects, 'clients': clients})

def submit_contact_form(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        city = request.POST['city']
        ContactFormSubmission.objects.create(full_name=full_name, email=email, mobile_number=mobile_number, city=city)
        messages.success(request, "Form submitted successfully!")
        return redirect('landing_page')

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        NewsletterSubscription.objects.create(email=email)
        messages.success(request, "Subscribed successfully!")
        return redirect('landing_page')
