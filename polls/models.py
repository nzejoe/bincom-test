from django.db import models
from django.utils.timezone import now


class AgentName(models.Model):
    name_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(auto_created=True, primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.lga_name


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(auto_created=True, primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.polling_unit_uniqueid
