from django.shortcuts import redirect, render
from .models import Blog, Contact
from .forms import BlogForm
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    # return HttpResponse("Hello, This is Bishal's Project")
    blog = Blog.objects.all() 
    return render(request,"crud/index.html",{"Blogs":blog})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        crud = Contact(
            name = name,
            email= email,
            message = message
        )
        crud.save()


    return render(request,"crud/contacts.html")

def particularData(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,"crud/index.html",{"blog":blog})


def create(request):
    forms = BlogForm(request.POST or None)
    if(forms.is_valid()):
        forms.save()
        return redirect("home")
    return render(request, "crud/create.html",{"forms":forms})