from django.db import models
import datetime
from taggit.managers import TaggableManager

# List of tags (e.g. K-On Season 1)
class Tag(models.Model):
    name = models.CharField(max_length=200)
    associated_tags = models.ManyToManyField("self", symmetrical=False)
    def __str__(self):
        for tag in self.associated_tags.all():
            print("Associated tag: ", tag)
        return self.name

class Entry(models.Model):
    date = models.DateField()
    duration = models.IntegerField()
    comment = models.CharField(max_length=280)
    tags = models.ManyToManyField(Tag)
    auto_tags = TaggableManager()
    def __str__(self):
        return_str = ''
        duration_str = 'No duration'
        try:
            date_str = self.date.strftime('%Y-%m-%d')
        except:
            date_str = 'No date'
        try:
            duration_str = str(self.duration)
        except:
            duration_str = 'No duration'
        try:
            comment_str = str(self.comment)
        except:
            comment_str = 'No comment'
        return  (date_str + " for " + duration_str + " minutes\t Comment: " + comment_str)
    @property
    def get_html_url(self):
        url = reverse('entry_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
