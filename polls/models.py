from django.db import models
from django.utils.timezone import now


class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class LGA(models.Model):
    uniqueid = models.AutoField(auto_created=True, primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.lga_name


class Ward(models.Model):
    uniqueid = models.AutoField(auto_created=True, primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.ward_name


class PollingUnit(models.Model):
    uniqueid = models.AutoField(auto_created=True, primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField()
    polling_unit_number = models.CharField(max_length=50)
    polling_unit_name = models.CharField(max_length=50)
    polling_unit_description = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    entered_by_user = models.CharField(max_length=50, null=True, blank=True)
    date_entered = models.DateTimeField(default=now, null=True, blank=True)
    user_ip_address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.polling_unit_name


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


class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(auto_created=True, primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(auto_created=True, primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.ward_name


class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    def __str__(self):
        return self.partyname
