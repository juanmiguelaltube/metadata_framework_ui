from django.db import models
from django import forms 
from django.utils.translation import gettext_lazy as _


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

    def __str__(self):
        return f"{self.cbs.code}:{self.data_source.code}:{self.field}"


class Metadata(models.Model):
    schema_field = models.ForeignKey(SchemaField,on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory,on_delete=models.CASCADE)
    params = models.CharField(max_length=255)
    
    class Meta:
        ordering = ["schema_field"]
        verbose_name_plural = "Metadata"

    def __str__(self):
        return f"{self.schema_field}"
