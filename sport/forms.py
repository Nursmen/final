from django import forms

from .models import *

class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('title', 'text', 'repeat', )

class ProgramForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = ('title', 'text', 'image', )

class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('number', 'program', 'exercises', )