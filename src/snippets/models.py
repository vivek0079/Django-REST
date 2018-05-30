from django.db import models
from rest_framework.reverse import reverse 
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    title       = models.CharField(max_length=100, blank=True, default='')
    code        = models.TextField()
    line_nos    = models.BooleanField(default=False)
    url         = models.URLField()
    language    = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style       = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['timestamp',]
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'
    

    def get_api_url(self, request=None):
        return reverse("snippets:snippet-rud", kwargs={'pk': self.id}, request=request)

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title
