from django.contrib.auth.models import User
from django.db import models


class WorkoutPlan(models.Model):
    """
    A plan or collection of workouts
    """
    user = models.ForeignKey(User, help_text="Creator of workout plan")
    name = models.CharField(max_length=255)
    notes = models.TextField()


class Workout(models.Model):
    """
    A collection of exercises
    """
    plan = models.ForeignKey(WorkoutPlan)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    notes = models.TextField()

    class Meta:
        ordering = ['order']


class Exercise(models.Model):
    """
    An exercise
    """
    workout = models.ForeignKey(Workout)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    notes = models.TextField()

    class Meta:
        ordering = ['order']


class Set(models.Model):
    """
    A set
    """
    UNITS = (
        (1, 'lbs'),
        (2, 'kgs'),
    )
    exercise = models.ForeignKey(Exercise)
    reps = models.CharField(max_length=10)
    weight = models.PositiveIntegerField(default=0)
    units = models.PositiveIntegerField(choices=UNITS, default=1)


class UserWorkoutPlan(models.Model):
    """
    A workout plan owned by a user
    """
    user = models.ForeignKey(User, help_text="Workout plan used by user")
    plan = models.ForeignKey(WorkoutPlan)
    workout = models.PositiveIntegerField(help_text="Which workout are you on")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class UserSet(models.Model):
    """
    A set a user has done
    """
    UNITS = (
        (1, 'lbs'),
        (2, 'kgs'),
    )
    user = models.ForeignKey(User)
    exercise = models.ForeignKey(Exercise)
    reps = models.CharField(max_length=10)
    weight = models.PositiveIntegerField(default=0)
    units = models.PositiveIntegerField(choices=UNITS, default=1)
    created = models.DateTimeField(auto_now_add=True)
