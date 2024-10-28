import os
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from mainpage.form import sendmessageform

# Create your views here.
def homepageview(request):
    homesection = HomesectionModel.objects.all().values()
    bio = BiolinkModel.objects.all().values()
    template = loader.get_template('homepage.html')
    context = {'content': homesection, 'bio_content': bio}
    return HttpResponse(template.render(context, request))

def aboutmeview(request):
    template = loader.get_template('aboutme.html')
    institution = InstitutionModel.objects.all().values()
    description = DescriptionModel.objects.first()
    bio = BiolinkModel.objects.all().values()
    context = {'institution': institution, 'bio_content': bio, 'description': description}
    return HttpResponse(template.render(context, request))

def portfolioview(request):
    templates = loader.get_template('portfolio.html')
    portfolio = PortfolioModel.objects.all().values()
    description = DescriptionModel.objects.first()
    bio = BiolinkModel.objects.all().values()
    context = {'portfolio': portfolio, 'bio_content': bio, 'description': description}
    return HttpResponse(templates.render(context, request))

def contactview(request):
    template = loader.get_template('contact.html')
    bio = BiolinkModel.objects.all().values()  
    description = DescriptionModel.objects.first()  
    form = sendmessageform(request.POST)
    if (request.method == 'POST'):        
        if (form.is_valid()):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact = ContactModel.objects.create(name=name, email=email, message=message)
            contact.save()
            return HttpResponse("Form submitted successfully...")
        else:
            return HttpResponse('Please fillup the form with correct information')
    context = {'bio_content': bio, 'form': form, 'description': description}
    return HttpResponse(template.render(context, request))

def blogview(request):
    template = loader.get_template('blog.html')
    bio = BiolinkModel.objects.all().values()  
    blog = BlogModel.objects.all().values()
    context = {'bio_content': bio, 'blog': blog}
    return HttpResponse(template.render(context, request))