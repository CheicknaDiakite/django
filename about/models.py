from django.db import models
from django.utils.text import slugify

# Create your models here.
class About(models.Model):
    titre = models.CharField(max_length=100, null=True, blank=False)
    libelle = models.CharField(max_length=255, null=True, blank=False)
    image = models.ImageField()
    description = models.CharField(max_length=255, null=True, blank=False)

    slug = models.SlugField(editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def all_categorie(self):
        return self.cate_about_set.all()
    
    def __str__(self):
        return self.titre

    def _get_unique_slug(self):
        slug = slugify(self.slug)
        unique_slug = slug
        num = 1
        while About.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Cate_About(models.Model):
    libelle = models.CharField(max_length=255, null=True, blank=False)

    about = models.ForeignKey(About, on_delete=models.CASCADE)