

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from configapp.models import Viloyat, Tuman, Mahalla


Viloyat.objects.filter(id=3).update(
    title="Yangilangan Viloyat",
    context="Yangilangan viloyat haqida"
)

Tuman.objects.filter(id=3).update(
    title="Yangilangan Tuman",
    context="Yangilangan tuman haqida"
)

Mahalla.objects.filter(id=3).update(
    title="Yangilangan Mahalla",
    context="Yangilangan mahalla haqida"
)

print("UPDATE: id=3 bo‘lgan ma'lumotlar yangilandi.")
