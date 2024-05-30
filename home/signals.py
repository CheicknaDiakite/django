from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Slide



@receiver(post_save, sender=Slide)
def ensure_single_instance(sender, instance, **kwargs):
    # Récupérer tous les enregistrements sauf l'instance actuelle
    other_instances = Slide.objects.exclude(id=instance.id)

    # Supprimer tous les autres enregistrements
    if other_instances.exists():
        other_instances.delete()
