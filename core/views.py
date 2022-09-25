from django.shortcuts import render
from .models import Blog
def home(request):
    context = {'posts': Blog.objects.all()}
    return render(request, 'core/home.html', context=context)
def about(request):
    return render(request, 'core/about.html')
def contact(request):

    return render(request, 'core/contact.html')
