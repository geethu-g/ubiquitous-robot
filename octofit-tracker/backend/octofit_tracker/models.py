from djongo import models
from bson import ObjectId


class User(models.Model):
    id = models.ObjectIdField(
        primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Team(models.Model):
    id = models.ObjectIdField(
        primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=50, unique=True)
    members = models.JSONField(default=list)

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.ObjectIdField(
        primary_key=True, default=ObjectId, editable=False)
    user = models.EmailField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.activity}"


class Leaderboard(models.Model):
    id = models.ObjectIdField(
        primary_key=True, default=ObjectId, editable=False)
    team = models.CharField(max_length=50)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team}: {self.points}"


class Workout(models.Model):
    id = models.ObjectIdField(
        primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
