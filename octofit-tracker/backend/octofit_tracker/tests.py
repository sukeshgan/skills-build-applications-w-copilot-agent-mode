from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')
    def test_user_create(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Bruce Wayne', email='bruce@wayne.com', team=team)
        self.assertEqual(str(user), 'Bruce Wayne')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')
    def test_activity_create(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=team)
        workout = Workout.objects.create(name='Iron Training', description='Suit up', difficulty='Hard')
        activity = Activity.objects.create(user=user, workout=workout, date='2026-05-16', duration=60, calories_burned=500)
        self.assertEqual(str(activity), 'Tony Stark - Iron Training on 2026-05-16')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='DC', description='DC Team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=1000, rank=1)
        self.assertEqual(str(leaderboard), 'DC - Rank 1')
