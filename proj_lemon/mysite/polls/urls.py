# (As instructed) Created this myself to match up with the things in views.py
# in this directory level.

from django.urls import path
from . import views

NOTES_2 = """
If you get an error page here, check that you’re going to 
        http://localhost:8000/polls/ 
and not http://localhost:8000/.
"""

urlpatterns = [
    path('', views.index, name='index'),
    # above: the empty url path should run the index function in views.py

]

NOTES_1 = """
The include() function allows referencing other URLconfs. 
Whenever Django encounters include(), it chops off whatever part 
of the URL matched up to that point and sends the remaining string to 
the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. 
Since polls are in their own URLconf (polls/urls.py), they can be 
placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, 
or any other path root, and the app will still work.
"""