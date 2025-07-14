

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from configapp.models import Viloyat, Tuman, Mahalla

v1 = Viloyat.objects.create(title="Toshkent", context="Poytaxt")
v2 = Viloyat.objects.create(title="Farg'ona", context="Vodiy")
v3 = Viloyat.objects.create(title="Samarqand", context="Tarixiy shahar")

for v in Viloyat.objects.all():
    for i in range(1, 4):
        Tuman.objects.create(
            viloyat=v,
            title=f"{v.title} Tuman {i}",
            context=f"{v.title} tuman {i} haqida"
        )

for t in Tuman.objects.all():
    for i in range(1, 4):
        Mahalla.objects.create(
            tuman=t,
            title=f"{t.title} Mahalla {i}",
            context=f"{t.title} mahalla {i} haqida"
        )

print("INSERT: Viloyat, Tuman va Mahalla ma'lumotlari yaratildi.")
