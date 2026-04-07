from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team']

    def get_id(self, obj):
        return str(getattr(obj, '_id', None) or obj.pk)

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

    def get_id(self, obj):
        return str(getattr(obj, '_id', None) or obj.pk)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity', 'duration']

    def get_id(self, obj):
        return str(getattr(obj, '_id', None) or obj.pk)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

    def get_id(self, obj):
        return str(getattr(obj, '_id', None) or obj.pk)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description']

    def get_id(self, obj):
        return str(getattr(obj, '_id', None) or obj.pk)
