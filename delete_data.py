

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from configapp.models import Viloyat, Tuman, Mahalla


Mahalla.objects.filter(id=1).delete()
Tuman.objects.filter(id=1).delete()
Viloyat.objects.filter(id=1).delete()

print("DELETE: id=1 bo‘lgan ma'lumotlar o‘chirildi.")
