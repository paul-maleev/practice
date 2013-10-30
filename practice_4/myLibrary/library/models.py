from django.db import models, connection
import datetime

<<<<<<< HEAD
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
# test
=======
# test

>>>>>>> Stashed changes


>>>>>>> Stashed changes
=======

>>>>>>> 3a15f11bda9e5f125b216df9b8aee234c9becc39
class Author(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):

    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())

    def get_absolute_url(self):
        curson = connection.cursor()
        curson.execute(
            "SELECT id FROM library_book WHERE title = %s", [self.title])
        return "/library/books/%s/" % curson.fetchall()[0]

    def __unicode__(self):
        return self.title


class Publisher(models.Model):

    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField(max_length=32)

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.title, self.city, self.country)
