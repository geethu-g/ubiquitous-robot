from django.test import TransactionTestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TransactionTestCase):
    def test_create_user(self):
        user = User.objects.create(
            name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.email, 'test@example.com')

    def test_user_str(self):
        user = User.objects.create(
            name='Alice', email='alice@example.com', team='DC')
        self.assertEqual(str(user), 'Alice')


class TeamModelTest(TransactionTestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', members=['test@example.com'])
        self.assertEqual(team.name, 'Marvel')

    def test_team_str(self):
        team = Team.objects.create(name='DC', members=[])
        self.assertEqual(str(team), 'DC')


class ActivityModelTest(TransactionTestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(
            user='test@example.com', activity='Run', duration=30)
        self.assertEqual(activity.activity, 'Run')

    def test_activity_str(self):
        activity = Activity.objects.create(
            user='bob@example.com', activity='Swim', duration=45)
        self.assertIn('bob@example.com', str(activity))


class LeaderboardModelTest(TransactionTestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(lb.points, 100)

    def test_leaderboard_str(self):
        lb = Leaderboard.objects.create(team='DC', points=200)
        self.assertIn('DC', str(lb))


class WorkoutModelTest(TransactionTestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Yoga', description='Relax')
        self.assertEqual(workout.name, 'Yoga')

    def test_workout_str(self):
        workout = Workout.objects.create(
            name='HIIT', description='High intensity')
        self.assertEqual(str(workout), 'HIIT')


class UserAPITest(APITestCase):
    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {'name': 'API User', 'email': 'apiuser@example.com',
                'team': 'Avengers'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], 'apiuser@example.com')


class TeamAPITest(APITestCase):
    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        data = {'name': 'Avengers', 'members': ['tony@example.com']}
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Avengers')


class ActivityAPITest(APITestCase):
    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity(self):
        data = {'user': 'runner@example.com', 'activity': 'Run',
                'duration': 30}
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['activity'], 'Run')


class LeaderboardAPITest(APITestCase):
    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_leaderboard_entry(self):
        data = {'team': 'Champions', 'points': 500}
        response = self.client.post('/api/leaderboard/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['points'], 500)


class WorkoutAPITest(APITestCase):
    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_workout(self):
        data = {'name': 'Pilates', 'description': 'Core strengthening'}
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Pilates')
