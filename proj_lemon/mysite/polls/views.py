from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# To call a view, we need to map it to a URL
# - and for this we use a URLconf
# To create a URLconf for this POLLS directory, create a new file
# called URLS.PY 
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

