#from json_field import JSONField
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, null=True)


class FavoriteThing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    ranking = models.IntegerField()
    #metadata = JSONField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_date_time = models.DateTimeField(auto_now_add=True)
    last_modified_date_time = models.DateTimeField(auto_now=True)

class AuditTrail(models.Model):
    id = models.AutoField(primary_key=True)
    favorite_thing = models.ForeignKey(FavoriteThing, on_delete=models.PROTECT)
    column_changed = models.CharField(max_length=30)
    old_value = models.CharField(max_length=100)
    new_value = models.CharField(max_length=100)
    modified_date_time = models.DateTimeField()