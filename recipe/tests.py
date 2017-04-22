from django.core.urlresolvers import resolve
from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Recipe, CookedAt
from . import views
from freezegun import freeze_time
