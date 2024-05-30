from django.db import models
from django.utils.text import slugify

# Create your models here.
class Equipe(models.Model):
    nom = models.CharField(max_length=200, null=False, blank=True)
    image = models.ImageField()
    fonction = models.CharField(max_length=250, null=False, blank=True)

    slug = models.SlugField(editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

    def _get_unique_slug(self):
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Equipe.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()