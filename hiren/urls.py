"""hiren URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from recipe import views
from django.contrib.auth import logout
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^create/', views.create, name='create'),
    url(r'^cuisine/(?P<cuisine>[^\.]+)/', views.cuisine),
    url(r'^meal/(?P<meal>[^\.]+)/', views.meal),
    url(r"^recipes/(?P<pk>[^\.]+)/edit/$", views.recipe_edit, name='recipe_edit'),
    url(r"^recipes/(?P<pk>[^\.]+)/$", views.recipe),
    url(r'^recipes/', views.recipes, name='recipes'),
    url(r'^logout/', logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
]
