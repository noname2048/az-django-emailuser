from django.db import models


class Book(models.Model):
    isbn13 = models.SlugField(max_length=13, db_index=True)
    title = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    author = models.CharField(max_length=40)


class Bookshelf(models.Model):
    user = models.ForeignKey("MyUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=40, db_index=True)


# class BookTag(models.Model):
#     level = models.IntegerField()
