from django.shortcuts import render

from about.models import About
from equipe.models import Equipe
from home.models import Slide
from contact.models import Contact
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from service.models import Service


def root_index(request):

    abouts = About.objects.all()
    slides = Slide.objects.all()
    services = Service.objects.all()
    equipes = Equipe.objects.all()

    context = {"abouts": abouts, 
               "services": services,
               "slides": slides,
               "equipes": equipes,               
               }

    if request.method == "POST":
        form_data = request.POST
        print(form_data)
        name = form_data.get("name")
        sujet = form_data.get("sujet")
        message = form_data.get("message")
        email = form_data.get("email")

        new_contact = Contact(name=name,
                            sujet=sujet,
                            message=message,
                            email=email,
                            )

        new_contact.save()
        message = (f"Merci {name} <br>"
                       f"Nous avons reussi votre message")

            
        cont = {"message": message,
                
                }

        html_info = render_to_string("email/email.html", cont)

        send_mail(
            sujet,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html_info)

        # TODO send mail

    return render(request, 'index.html', context)