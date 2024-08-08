from django.shortcuts import render, redirect
from .models import Service, Contact, BlogPost, Testimonial, Portfolio



def index(request):
    contacts = Contact.objects.all().order_by('harakatlar')
    services = Service.objects.all()
    blogs = BlogPost.objects.all()  
    testimonials = Testimonial.objects.all()
    portfolios = Portfolio.objects.all()
    return render(request, 'front/index.html', {'contacts':contacts, 'services': services, 'blogs': blogs, 'testimonials': testimonials, 'portfolios': portfolios})







