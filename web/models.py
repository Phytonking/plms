from django.db import models

# Create your models here.


class teams(models.Model):
    teamID = models.IntegerField()
    leader_name = models.TextField()
    leader_email = models.EmailField()
    leader_phone_number = models.IntegerField()
    team_name = models.TextField()
    points = models.IntegerField()
    team_type = models.TextField(null=True)
    def __str__(self):
        return f"{self.teamID} {self.team_name} {self.team_type}"



class participants(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    team = models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.team}"



class leaderboard(models.Model):
    name = models.TextField(null=True)
    level = models.IntegerField()
    def __str__(self):
        return f"{self.name}"