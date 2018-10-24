from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'real_events/index.html')

def all_news(request):
    return HttpResponse("all_news")
def news_post(request, news_post_slug):
    return HttpResponse("news_post")

def all_places(request):
    return HttpResponse("all_places")
def place(request, place_slug):
    return HttpResponse("place")

def all_meetings(request):
    return HttpResponse("all_meetings")
def meeting(request, meeting_slug):
    return HttpResponse("meeting")

def all_referees(request):
    return HttpResponse("all_referees")
def referee(request, referee_slug):
    return HttpResponse("referee")

def all_teams(request):
    return HttpResponse("all_teams")
def team(request, team_slug):
    return HttpResponse("team")

def all_members(request):
    return HttpResponse("all_members")
def member(request, member_slug):
    return HttpResponse("member")

def all_staff(request):
    return HttpResponse("all_staff")
def staff(request, place_slug):
    return HttpResponse("staff")


