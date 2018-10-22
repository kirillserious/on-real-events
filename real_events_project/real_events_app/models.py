from django.db import models
from django.utils.safestring import mark_safe

class Profession(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Place(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    photo = models.ImageField(blank=True)
    address = models.CharField(max_length=512, blank=True)
    info = models.CharField(max_length=2048, blank=True)
    city = models.CharField(max_length=128, blank=True)
    # location
    post = models.CharField(max_length=4096, blank=True)
    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photo.url)
        else:
            return 'No Photo'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

class Meeting(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    date = models.DateField()
    places = models.ManyToManyField(Place)
    photo = models.ImageField(blank=True)
    info = models.CharField(max_length=2048, blank=True)
    post = models.CharField(max_length=4096, blank=True)
    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photo.url)
        else:
            return 'No Photo'
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    photo = models.ImageField(blank=True)
    info = models.CharField(max_length=2048, blank=True)
    link = models.URLField(blank=True)
    post = models.CharField(max_length=4096, blank=True)
    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photo.url)
        else:
            return 'No Photo'
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.name

class Referee(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    photo = models.ImageField(blank=True)
    info = models.CharField(max_length=2048, blank=True)
    link = models.URLField(blank=True)
    post = models.CharField(max_length=4096, blank=True)
    meetings = models.ManyToManyField(Meeting)
    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photo.url)
        else:
            return 'No Photo'
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.name

class Team(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    photo = models.ImageField(blank=True)
    info = models.CharField(max_length=2048, blank=True)
    post = models.CharField(max_length=4096, blank=True)
    meetings = models.ManyToManyField(Meeting)
    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photo.url)
        else:
            return 'No Photo'
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    photo = models.ImageField(blank=True)
    info = models.CharField(max_length=2048, blank=True)
    link = models.URLField(blank=True)
    post = models.CharField(max_length=4096, blank=True)
    professions = models.ManyToManyField(Profession)
    teams = models.ManyToManyField(Team)
    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.photo.url)
        else:
            return 'No Photo'
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.name

class NewsPost(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    photo = models.ImageField(blank=True)
    info = models.CharField(max_length=2048, blank=True)
    date = models.DateField()
    post = models.CharField(max_length=4096, blank=True)
    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photo.url)
        else:
            return 'No Photo'
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.title