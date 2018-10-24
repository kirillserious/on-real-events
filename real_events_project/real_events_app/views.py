from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'real_events/index.html')

def all_news(request):
    return render(request, 'real_events/all_news.html')
def news_post(request, news_post_slug):
    return render(request, 'real_events/news_post.html')

def all_places(request):
    return render(request, 'real_events/all_places.html')
def place(request, place_slug):
    return render(request, 'real_events/place.html')

def all_meetings(request):
    return render(request, 'real_events/all_meetings.html')
def meeting(request, meeting_slug):
    return render(request, 'real_events/meeting.html')

def all_referees(request):
    return render(request, 'real_events/all_referees.html')
def referee(request, referee_slug):
    return render(request, 'real_events/referee.html')

def all_teams(request):
    return render(request, 'real_events/all_teams.html')
def team(request, team_slug):
    return render(request, 'real_events/team.html')

def all_members(request):
    return render(request, 'real_events/all_members.html')
def member(request, member_slug):
    return render(request, 'real_events/member.html')

def all_staff(request):
    return render(request, 'real_events/all_staff.html')
def staff(request, place_slug):
    return render(request, 'real_events/staff.html')


