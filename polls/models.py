from django.db import models


class AgentName(models.Model):
    name_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()
