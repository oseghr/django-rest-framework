from django.db import models


# Create your models here.


class ActiveLinkManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(active=True)

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    # author = get_user_model.ForeignKey() : A Foreign Key to the current user model. Make use of Django’s function.
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) 


    def __str__(self):
        return self.target_url
