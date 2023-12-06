from django.contrib import admin

from project1.models import TestModel

admin.site.register(TestModel)

from django.contrib import admin

from project1.models import Image

admin.site.register(Image)


def site(request):
    return None
