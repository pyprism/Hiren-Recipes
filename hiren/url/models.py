from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Url(models.Model):
    user = models.ForeignKey(User)
    full_url = models.URLField(max_length=2000, blank=False, null=False)
    short_url = models.TextField(max_length=10, blank=False, null=False, unique=True)
    counter = models.BigIntegerField(default=0)
    date = models.DateTimeField(blank=False, null=False)


class Details(models.Model):
    url_id = models.ForeignKey(Url)
    ip = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(max_length=100, blank=True, null=True)
    http_refferer = models.TextField(blank=True, null=True)