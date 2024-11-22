from django.contrib import admin
from .models import Project, Client, ContactFormSubmission, NewsletterSubscription

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(ContactFormSubmission)
admin.site.register(NewsletterSubscription)
