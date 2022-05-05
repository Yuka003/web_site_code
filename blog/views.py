from django.shortcuts import render, HttpResponse
from .models import Blog, Contact
from .forms import ContactForm
# Create your views here.


def home_page(request):
    context = {}
    blogs = Blog.objects.all()
    context["blogs"] = blogs


    return render(request, "home.html", context)


def contact_us(request):
    context = {}
    if request.POST:
        my_form = ContactForm(request.POST)
        if my_form.is_vaiid():
            my_form.save()

        else:
            context["errors"] = my_form.errors

        #new_contact = Contact.objects.create(
         #   first_name = request.POST['first_name'],
          #  last = request.POST['last_name'],
           # email = request.POST['email'],
            #message = request.POST['message']
            
            


    return render(request, "contact_us.html", context)


def blog_detail(request, pk):
    context = {}
    blog = Blog.objects.get(id=pk)
    context['blog'] = blog


    return render(request, "blog_detail.html", context)
