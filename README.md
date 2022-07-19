# final
final project for cs50
# Background
> I warn you in advance about translation errors. I am from Kyrgizstan and english is not my native language.

At the beginning of the summer, I became seriously interested in health issues. 
I started to train a long time ago according to the training program from the android application. Now I decided to try to collect the recommendations of a couple of familiar trainers and create a training program for myself (something like a hobby).
Workouts from the application is a complete record of all my workouts for about a month, skipping rest days. The program does not claim to be suitable for everyone. I just wanted to point out that I tried to take into account all the necessary elements that are required for such applications.

# Distinctiveness and Complexity
The program has nothing to do with what I have done earlier in this course. The basis of the program consists of three models of django. The first is the training programs, the second is the days in the program (I paused after a few days, so I decided to divide all the workouts into programs and they include a different number of days), the third is the exercises themselves, different levels of exercises mean an increase in complexity, repetitions, time.
Once you have done one day, it is marked in the "calendar" of the program in a different color, for ease of use. Also, the percentage of completed days is displayed on the programs page as a progress bar. All completed days will fill the scale to the end.
The tab for the exercises of a specific day implies a dropper with detailed information about the exercises, or about the necessary equipment. 
You can also create your own training program. To do this, you need to select a photo, write all the necessary information. Then, having created the necessary exercises, connect the exercises and the program by creating days.
I repeat, the program can have a different number of days, and the same day can have a different number of exercises (not enough of many similar sites).

## JS

I use this language for animations, buttons, moving to another address, sending information about the end of the day, without being forced to leave the page.
Mpbile responsive is achieved by means of boostrap and in some places css

# Files:
- `forms.py` - forms for creating things
- `cr_day.html`, cr_exrcise.html, cr_program.html - contain html for creating, can be in one file, but for me different files is easier to work
- `create.html` - html for base create page. from that you can go into `cr_day/exercise/program.html`. So in this page you can check list of all exercises
- `days.html` - 'calendar' with days for every program
- `exercises.html` - all programs (bad naming, but it sounds logical in my native language)
- `index.html` - layout
- `list.html` - exercises for the day. 

> i wrote css special for every html in html file

- `landing.html` - landing for final project

# Admin/debagging

In admin I just made more usefull ordering for models, so I created view called 'clear' with url '/exercise/clear'. If you go to that, site will automatically clear all prograss in app.
