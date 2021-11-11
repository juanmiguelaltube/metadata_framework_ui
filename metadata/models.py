from django.db import models
from django import forms 
from django.utils.translation import gettext_lazy as _

class CBS(models.Model):
    id = models.CharField(primary_key=True,max_length=3)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "CBS"

    def __str__(self):
        return f"{self.id}:{self.name}"

class DataSource(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}:{self.name}"

class Factory(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    description = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.id
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Factories"

class SchemaField(models.Model):
    cbs = models.ForeignKey(CBS,on_delete=models.CASCADE)
    data_source = models.ForeignKey(DataSource,on_delete=models.CASCADE)
    field = models.CharField(max_length=255)
    whitelist = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cbs.id}:{self.data_source.id}:{self.field}"

    class Meta:
        ordering = ["field"]
        verbose_name_plural = "Schema Fields"

class Metadata(models.Model):
    field = models.ForeignKey(SchemaField,on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory,on_delete=models.CASCADE)
    condition = models.CharField(max_length=255, blank=True)
    format_in = models.CharField(max_length=255,blank=True)
    format_out = models.CharField(max_length=255,blank=True)
    
    class Meta:
        ordering = ["field"]
        verbose_name_plural = "Metadatas"

    def __str__(self):
        return f"{self.field}:{self.factory}"