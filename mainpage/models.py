from django.db import models

# Create your models here.
class HomesectionModel(models.Model):
    text1 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mainpage/static/image')
    image_name = models.CharField(max_length=200, null=True)

class BiolinkModel(models.Model):
    site_title = models.CharField(max_length=20)
    site_link = models.CharField(max_length=200)
    icon_link = models.CharField(max_length=200)
    def __str__(self):
        return self.site_title
    
class InstitutionModel(models.Model):
    image = models.ImageField(upload_to='mainpage/static/image')
    image_name = models.CharField(max_length=200)
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class PortfolioModel(models.Model):
    youtube_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)
    title = models.CharField(max_length=90)
    description = models.TextField(null=True)
    language = models.CharField(max_length=200, null=True)
    software = models.CharField(null=True, max_length=200, blank=True)
    def __str__(self):
        return self.title

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.email
    
class DescriptionModel(models.Model):
    about_description = models.TextField()
    portfolio_description = models.TextField()
    contact_description = models.TextField()

class BlogModel(models.Model):
    image = models.ImageField(upload_to='mainpage/static/image')
    image_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title