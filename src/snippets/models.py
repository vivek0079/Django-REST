from django.db import models
from django.contrib.auth import get_user_model

from rest_framework.reverse import reverse 

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

User = get_user_model()

class Snippet(models.Model):
    owner       = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)
    title       = models.CharField(max_length=100, blank=True, default='')
    code        = models.TextField()
    highlighted = models.TextField()
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
    
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title


    def get_api_url(self, request=None):
        return reverse("snippets:snippet-detail", kwargs={'pk': self.id}, request=request)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        line_nos = 'table' if self.line_nos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, line_nos=line_nos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
