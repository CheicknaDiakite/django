from django.db import models
from django.utils.text import slugify

# Create your models here.
class Service(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField()

    slug = models.SlugField(editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def all_categorie(self):
        return self.cate_service_set.all()

    def __str__(self):
        return self.nom

    def _get_unique_slug(self):
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Service.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

class Cate_Service(models.Model):
    libelle = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField()

    service = models.ForeignKey(Service, on_delete=models.CASCADE)