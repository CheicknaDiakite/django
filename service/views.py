from django.shortcuts import redirect, render

from .models import Cate_Service, Service

# Create your views here.

def service(request):
    services = Service.objects.all()

    context = {"services": services}

    if request.method == "POST":
        form_data = request.POST

        nom = form_data.get("nom")
        image = form_data.get("image")

        new_service = Service(nom=nom,
                            image=image,
                            )

        new_service.save()

    return render(request, "service/service.html", context)


def service_edit(request, slug):
    
    about = Service.objects.all().filter(slug=slug).first()

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


def service_delete(request, slug):
    about = Service.objects.all().filter(slug=slug).first()

    if about:
        about.delete()

    return redirect('app_client')


def service_category(request, slug):
    service = Service.objects.all().filter(slug=slug).first()
    cate_services = Cate_Service.objects.all()

    context = {"service": service,
               "cate_services": cate_services,
               }

    if request.method == "POST":
        form_data = request.POST

        libelle = form_data.get("libelle")
        description = form_data.get("description")
        service_slug = form_data.get("service")

        service = Service.objects.all().filter(slug=service_slug).first()
        if service:

            new_cate = Cate_Service(libelle=libelle,
                                description=description,
                                service=service,
                                )

            new_cate.save()

    return render(request, "service/categorie.html", context)


def service_category_edit(request, slug):
    cate = Cate_Service.objects.all().filter(slug=slug).first()

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


def service_category_delete(request, slug):
    categorie = Cate_Service.objects.all().filter(slug=slug).first()

    if categorie:
        categorie.delete()

    return redirect('app_client')
