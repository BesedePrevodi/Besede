from django.contrib import admin

# Register your models here.

from .models import Sklop, Beseda, Nivo

admin.site.register(Nivo)
admin.site.register(Sklop)
admin.site.register(Beseda)
