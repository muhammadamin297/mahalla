from django.db import models

class Viloyat(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()

    def __str__(self):
        return self.title

class Tuman(models.Model):
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Mahalla(models.Model):
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
