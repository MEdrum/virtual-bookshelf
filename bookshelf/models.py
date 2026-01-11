import uuid

from django.db import models

class Book(models.Model):
    bookID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn = models.CharField(max_length=17, unique=True) #13 characters with 4 hyphens
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    year_of_publication = models.IntegerField(blank=True, null=True)
    visibility = {
        "0": "private",
        "1": "friends",
        "2": "public",
    }
    borrowable = models.BooleanField(default=True)
    ownerID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    shelfID = models.ForeignKey('Shelf', on_delete=models.CASCADE)
    coverURL = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Shelf(models.Model):
    shelfID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    ownerID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
