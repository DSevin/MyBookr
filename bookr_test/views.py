from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def greeting_view(request):
    """Greet the user"""
    return HttpResponse("Hey there welcome to bookr, Your one stop place to review books")

def greeting_view_user(request):
    """Greeting view for the user"""
    user = request.user
    return HttpResponse("Welcome to Bookr! {username}".format(username =user))
