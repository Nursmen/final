from django.shortcuts import render, redirect
from .models import *

import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Count
from .forms import *

# Create your views here.
def index(request):
    programs = Program.objects.all().order_by('title')
    return render(request, 'sport/exercises.html', {'programs':programs})

def days(request, title):
    '''
        title - program title
    '''
    days = Day.objects.all().filter(program = Program.objects.get(title=title))
    need = 30 - len(days)
    return render(request, 'sport/days.html', {'days':days, 'need':range(need)})

def list(request, day, program):
    day = Day.objects.get(number=day, program = Program.objects.get(title=program))
    exercises = day.exercises.all()
    number = day.number
    return render(request, 'sport/list.html', {'exercises':exercises, 'number':number, 'program':program})

@csrf_exempt
@login_required
def add(request, day, program):
    try:
        program = Program.objects.get(title=program)
        day = Day.objects.get(number=day, program=program)
    except Day.DoesNotExist:
        return JsonResponse({"error": "Email not found."}, status=404)

    if (day.done != True):
        days = len(Day.objects.annotate(number_of_answers=Count('program')).filter(program=program))
        program.done += 100/days
        program.save()
        print(days)

    day.done = True
    day.save()


    return JsonResponse({'':''})

def clean(request):
    days = Day.objects.all()
    programs = Program.objects.all()

    for day in days:
        day.done = False
        day.save()

    for program in programs:
        program.done = 0
        program.save()

    return redirect('index')

def create_choise(request):
    exercises = Exercise.objects.all().order_by('text')
    return render(request, 'sport/create.html', {'exercises':exercises})

def create_element(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.save()
        return redirect('create')
    form = ExerciseForm()
    return render(request, 'sport/cr_exercise.html', {'form':form})

def create_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.done = 0
            program.save()
        return redirect('create')
    form = ProgramForm()
    return render(request, 'sport/cr_program.html', {'form':form})

def create_day(request):
    if request.method == 'POST':
        form = DayForm(request.POST)
        if form.is_valid():
            day = form.save(commit=False)
            day.done = False
            day.save()
            form.save_m2m()
        return redirect('create')
    form = DayForm()
    return render(request, 'sport/cr_day.html', {'form':form})