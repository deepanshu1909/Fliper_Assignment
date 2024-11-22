from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name

class ContactFormSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

class NewsletterSubscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
