from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data using Django ORM'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample data
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com",
             "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com",
             "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com",
             "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com",
             "team": "Marvel"},
        ]
        teams = [
            {"name": "Marvel", "members": [
                "ironman@marvel.com", "cap@marvel.com", "widow@marvel.com"]},
            {"name": "DC", "members": [
                "superman@dc.com", "batman@dc.com", "wonderwoman@dc.com"]},
        ]
        activities = [
            {"user": "superman@dc.com", "activity": "Flight",
             "duration": 60},
            {"user": "ironman@marvel.com", "activity": "Suit Training",
             "duration": 45},
        ]
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 120},
        ]
        workouts = [
            {"name": "Strength Training", "description": "Full body workout"},
            {"name": "Cardio Blast", "description": "High intensity cardio"},
        ]

        for user in users:
            user.pop('id', None)
            User(**user).save()
        for team in teams:
            team.pop('id', None)
            Team(**team).save()
        for activity in activities:
            activity.pop('id', None)
            Activity(**activity).save()
        for entry in leaderboard:
            entry.pop('id', None)
            Leaderboard(**entry).save()
        for workout in workouts:
            workout.pop('id', None)
            Workout(**workout).save()

        self.stdout.write(self.style.SUCCESS(
            'octofit_db database populated with test data using Django ORM.'))
