from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# We will write our endpoints here
# Endpoint -> a location on the web server we are going to

# Take a request and return a response
def main(request):
    return HttpResponse("<h1>Hello</h1>")
