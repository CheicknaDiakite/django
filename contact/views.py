from django.shortcuts import render

# Create your views here.

# Create your views here.
def contact(request):
    
    return render(request, "contact/contact.html", )


def about_edit(request, slug):
    
    
    return render(request, "app/edit_client.html")


def about_delete(request, slug):
  ...

def about_category(request):
    
    return render(request, "app/client.html")

