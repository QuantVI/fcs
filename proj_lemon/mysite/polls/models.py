from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

NOTES_1 = """
In our poll app, we’ll create two models: Question and Choice. 
    A Question has a question and a publication date. 
    A Choice has two fields: the text of the choice and a vote tally. 
Each Choice is associated with a Question
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, 
    on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

NOTES_2 = """
By running makemigrations, you’re telling Django that you’ve made some 
changes to your models (in this case, you’ve made new ones) and that 
you’d like the changes to be stored as a migration.

Migrations are how Django stores changes to your models 
(and thus your database schema) - they’re files on disk. 
You can read the migration for your new model if you like; 
it’s the file polls/migrations/0001_initial.py.
"""

NOTES_3 = """
The sqlmigrate command takes migration names and returns their SQL:
    $ python manage.py sqlmigrate polls 0001

https://docs.djangoproject.com/en/4.1/intro/tutorial02/
"""

NOTES_4 = """
for now, remember the three-step guide to making model changes:

- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.
"""