from django.contrib import admin
from HVApp.models.usuarios import User
from HVApp.models.hojaDeVida import HojaDeVida

# Register your models here.
admin.site.register(User)
admin.site.register(HojaDeVida)