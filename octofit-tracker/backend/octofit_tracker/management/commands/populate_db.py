from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        tony = User.objects.create(name='Tony Stark', email='tony@stark.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        flying = Workout.objects.create(name='Flying', description='Superhero flight', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=tony, workout=pushups, date=timezone.now().date(), duration=30, calories_burned=200)
        Activity.objects.create(user=steve, workout=running, date=timezone.now().date(), duration=45, calories_burned=400)
        Activity.objects.create(user=bruce, workout=pushups, date=timezone.now().date(), duration=20, calories_burned=150)
        Activity.objects.create(user=clark, workout=flying, date=timezone.now().date(), duration=60, calories_burned=600)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, total_points=600, rank=1)
        Leaderboard.objects.create(team=dc, total_points=750, rank=2)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
