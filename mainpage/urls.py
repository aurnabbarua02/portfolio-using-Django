from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepageview, name="homepage"),
    path('aboutme/', views.aboutmeview, name="aboutme"),
    path('portfolio/', views.portfolioview, name='portfolio'),
    path('contact/', views.contactview, name="contact"),
    path('blog/', views.blogview, name="blog"),
]