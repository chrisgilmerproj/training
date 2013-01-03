from django.contrib import admin

from workout.models import WorkoutPlan, Workout, Exercise, Set


class SetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Set, SetAdmin)


class SetInline(admin.TabularInline):
    model = Set
    extra = 3


class ExerciseAdmin(admin.ModelAdmin):
    inlines = [SetInline]

admin.site.register(Exercise, ExerciseAdmin)


class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]

admin.site.register(Workout, WorkoutAdmin)


class WorkoutInline(admin.TabularInline):
    model = Workout
    extra = 1


class WorkoutPlanAdmin(admin.ModelAdmin):
    inlines = [WorkoutInline]

admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
