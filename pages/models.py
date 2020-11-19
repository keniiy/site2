from django.db import models

# Create your models here.
from django.forms import ModelForm

class Booking(models.Model):
    TYPE_OF_TRAINING = (
        ('lesbian bdsm secret training', 'lesbian bdsm secret training'),
        ('gay bdsm secret training', 'gay bdsm secret training'),
        ('shemale secret training', 'shemale secret training'),
        ('gay/shemale secret training', 'gay/shemale secret training'),
    )
    COCK_ENLARGEMENT = (
        ('yes', 'yes'),
        ('no', 'no')
    )
    ASSHOLE_CREAM_ENLARGEMENT = (
        ('yes', 'yes'),
        ('no', 'no')
    )
    TIT_ENLARGEMENT = (
        ('yes', 'yes'),
        ('no', 'no')
    )
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False')
    )
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    training = models.CharField(max_length=28, choices=TYPE_OF_TRAINING, default='lesbian bdsm secret training')
    cock = models.CharField(max_length=10, choices=COCK_ENLARGEMENT, default='yes')
    address = models.CharField(max_length=100, blank=True)
    asshole_cream = models.CharField(max_length=10, choices=ASSHOLE_CREAM_ENLARGEMENT, default='yes')
    asshole_enlargement_cream = models.CharField(max_length=10, choices=TIT_ENLARGEMENT, default='yes')
    status = models.CharField(max_length=10, choices=STATUS, default='New')

    def __str__(self):
        return self.name




class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=250, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')

    def __str__(self):
        return self.name


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']