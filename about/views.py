from django.shortcuts import redirect, render

from .models import About, Cate_About

# Create your views here.
def about(request):
    abouts = About.objects.all()
    cate_abouts = Cate_About.objects.all()

    context = {"abouts": abouts,
               "cate_abouts": cate_abouts,
               }

    if request.method == "POST":
        form_data = request.POST

        titre = form_data.get("titre")
        libelle = form_data.get("libelle")
        image = form_data.get("image")
        description = form_data.get("description")

        new_about = About(titre=titre,
                            libelle=libelle,
                            image=image,
                            description=description,
                            )

        new_about.save()

    return render(request, "about/about.html", context)


def about_edit(request, slug):
    
    about = About.objects.all().filter(slug=slug).first()

    context = {"about": about}

    if request.method == "POST":
        form = request.POST

        titre = form.get("titre")
        if titre:
            about.titre = titre
            about.save()

        libelle = form.get("libelle")
        if libelle:
            about.libelle = libelle
            about.save()

        image = form.get("image")
        if image:
            about.image = image
            about.save()

        description = form.get("description")
        if description:
            about.description = description
            about.save()

        
        return redirect('app_client')

    return render(request, "app/edit_client.html", context)


def about_delete(request, slug):
    about = About.objects.all().filter(slug=slug).first()

    if about:
        about.delete()

    return redirect('app_client')


def about_category(request, slug):
    about = About.objects.all().filter(slug=slug).first()
    cate_abouts = Cate_About.objects.all()

    context = {"about": about,
               "cate_abouts": cate_abouts
               }

    if request.method == "POST":
        form_data = request.POST
       
        libelle = form_data.get("libelle")
        about_slug = form_data.get("about")

        about = About.objects.all().filter(slug=about_slug).first()
        if about:
            new_cate = Cate_About(libelle=libelle,
                                about=about,
                                )

            new_cate.save()

    return render(request, "about/categorie.html", context)


def about_category_edit(request, slug):
    cate = Cate_About.objects.all().filter(slug=slug).first()

    context = {"cate": cate}

    if request.method == "POST":
        form = request.POST

        libelle = form.get("libelle")
        if libelle:
            cate.libelle = libelle
            cate.save()

        about = form.get("about")
        if about:
            about.about = about
            about.save()
        
        return redirect('app_client')

    return render(request, "app/edit_client.html", context)


def about_category_delete(request, slug):
    categorie = Cate_About.objects.all().filter(slug=slug).first()

    if categorie:
        categorie.delete()

    return redirect('app_client')
