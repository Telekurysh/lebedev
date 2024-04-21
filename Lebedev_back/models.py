from django.db import models


class Movie(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    nativeId = models.CharField(max_length=100)
    nativeName = models.CharField(max_length=100)
    # Добавьте остальные поля из вашей модели
