from django.db import models
import datetime

# List of tags (e.g. K-On Season 1)
class Tag(models.Model):
    name = models.CharField(max_length=200)
    associated_tags = models.ManyToManyField("self", symmetrical=False)
    def __str__(self):
        for tag in self.associated_tags.all():
            print("Associated tag: ", tag)
        return self.name

class Entry(models.Model):
    date = models.DateTimeField()
    duration = models.IntegerField()
    comment = models.CharField(max_length=280)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return (self.date.strftime('%Y-%m-%d') + " for " + str(self.duration) + " minutes\t Comment: " + self.comment)

# from tracker.models import Entry, Tag
# Tag.objects.all()
