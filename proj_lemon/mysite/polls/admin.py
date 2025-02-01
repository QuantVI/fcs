from django.contrib import admin

# Register your models here.

NOTES_1 = """
But where’s our poll app? It’s not displayed on the admin index page.

Only one more thing to do: we need to tell the admin that 
Question objects have an admin interface. 
To do this, open the polls/admin.py file, and edit it 
(to import the Question object, and register it)
"""

from .models import Question

admin.site.register(Question)