from django.db import models

# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=255)
    done = models.IntegerField(default=0)
    image = models.URLField(blank=True,null=True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    repeat = models.IntegerField(default=30)

    def __str__(self) -> str:
        return self.title

class Day(models.Model):
    number = models.CharField(max_length=2)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True, default=None)
    done = models.BooleanField(default=False)
    exercises = models.ManyToManyField(Exercise, related_name='exercise', blank=True)


    def __str__(self) -> str:
        return f'{self.program} - {self.number}'