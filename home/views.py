from django.shortcuts import render

from .models import Slide

# Create your views here.

def home(request):
    homes = Slide.objects.all()

    context = {"homes": homes}

    if request.method == "POST":
        form_data = request.POST

        nom = form_data.get("nom")
        description = form_data.get("description")

        new_about = Slide(nom=nom,
                        description=description,
                            )

        new_about.save()

    return render(request, "home/home.html", context)

