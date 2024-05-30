from django.shortcuts import redirect, render

from .models import Equipe

# Create your views here.

# Create your views here.
def equipe(request):
    equipes = Equipe.objects.all()

    context = {"equipes": equipes}

    if request.method == "POST":
        form_data = request.POST

        nom = form_data.get("nom")
        fonction = form_data.get("fonction")
        image = form_data.get("image")
        
        new_about = Equipe(nom=nom,
                            fonction=fonction,
                            image=image,
                            )

        new_about.save()

    return render(request, "equipe/equipe.html", context)


def equipe_edit(request, slug):
    
    equipe = Equipe.objects.all().filter(slug=slug).first()

    context = {"equipe": equipe}

    if request.method == "POST":
        form = request.POST

        titre = form.get("titre")
        if titre:
            equipe.titre = titre
            equipe.save()

        libelle = form.get("libelle")
        if libelle:
            equipe.libelle = libelle
            equipe.save()

        image = form.get("image")
        if image:
            equipe.image = image
            equipe.save()

        description = form.get("description")
        if description:
            equipe.description = description
            equipe.save()

        
        return redirect('app_client')

    return render(request, "app/edit_client.html", context)


def equipe_delete(request, slug):
    equipe = Equipe.objects.all().filter(slug=slug).first()

    if equipe:
        equipe.delete()

    return redirect('app_client')


def equipe_category(request):
    
    return render(request, "app/client.html")

