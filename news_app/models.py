from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):

    nomi = models.CharField(max_length=50)


    def __str__(self):
        return self.nomi


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = News.Status.Publish)


class News(models.Model):

    class Status(models.TextChoices):
        Draft = 'DR', "Draft"
        Publish = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    views = models.IntegerField(default=0)

    published = PublishManager()
    objects = models.Manager()

    class Meta:
        ordering = ['-published_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', kwargs={'slug': self.slug})


class Contact(models.Model):

    user = models.CharField(max_length=150)
    email = models.EmailField()
    msg = models.TextField()


    def __str__(self):
        return self.user
























