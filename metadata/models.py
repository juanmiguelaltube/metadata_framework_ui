from django.db import models
from django import forms 
from django.utils.translation import gettext_lazy as _
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class CBS(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["code"]
        verbose_name_plural = "CBS"

    def __str__(self):
        return f"{self.code}:{self.name}"

class DataSource(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code}:{self.name}"

class Factory(models.Model):
    factory_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.factory_name

class SchemaField(models.Model):
    cbs = models.ForeignKey(CBS,on_delete=models.CASCADE)
    data_source = models.ForeignKey(DataSource,on_delete=models.CASCADE)
    field = models.CharField(max_length=255)
    whitelist = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cbs.code}:{self.data_source.code}:{self.field}"


class Metadata(models.Model):
    field = models.ForeignKey(SchemaField,on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory,on_delete=models.CASCADE)
    condition = models.CharField(max_length=255, blank=True)
    format_in = models.CharField(max_length=255,blank=True)
    format_out = models.CharField(max_length=255,blank=True)
    
    class Meta:
        ordering = ["field"]
        verbose_name_plural = "Metadata"

    def __str__(self):
        return f"{self.field}:{self.factory}"