from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.

class Widget(models.Model):

    title = models.CharField(max_length=100)
    content = HTMLField()

    show_in_widget = models.BooleanField()


    class Meta:
        verbose_name = _("Widget")
        verbose_name_plural = _("Widgets")
#        ordering = ("-created_at",)
