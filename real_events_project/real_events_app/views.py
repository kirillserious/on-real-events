from django.shortcuts import render
from django.http import HttpResponse, Http404

from real_events_app.models import Profession, Place, Meeting, Staff, Referee, Member, Team, NewsPost

def __get_model_by_slag(object, slug):
    try:
        return object.objects.get(slug=slug)
    except:
        raise Http404("")

def index(request):
    return render(request, 'real_events/index.html')

def all_news(request):
    context_dict = {}
    context_dict['obj'] = NewsPost.objects.all().order_by('-date')
    return render(request, 'real_events/all_news.html', context_dict)
def news_post(request, slug):
    context_dict = {}
    context_dict['obj'] = __get_model_by_slag(NewsPost, slug)
    return render(request, 'real_events/news_post.html', context_dict)

def all_places(request):
    context_dict = {}
    context_dict['obj'] = Place.objects.all()
    return render(request, 'real_events/all_places.html', context_dict)
def place(request, slug):
    context_dict = {}
    context_dict['obj'] = __get_model_by_slag(Place, slug)
    return render(request, 'real_events/place.html', context_dict)

def all_meetings(request):
    context_dict = {}
    context_dict['obj'] = Meeting.objects.all()
    return render(request, 'real_events/all_meetings.html', context_dict)
def meeting(request, slug):
    context_dict = {}
    context_dict['obj'] = __get_model_by_slag(Meeting, slug)

    return render(request, 'real_events/meeting.html', context_dict)

def all_referees(request):
    context_dict = {}
    context_dict['obj'] = Referee.objects.all()
    return render(request, 'real_events/all_referees.html', context_dict)
def referee(request, slug):
    context_dict = {}
    context_dict['obj'] = __get_model_by_slag(Referee, slug)
    return render(request, 'real_events/referee.html', context_dict)

def all_teams(request):
    context_dict = {}
    context_dict['obj'] = Team.objects.all()
    return render(request, 'real_events/all_teams.html', context_dict)
def team(request, slug):
    context_dict = {}
    context_dict['obj'] = __get_model_by_slag(Team, slug)
    context_dict['members'] = Member.objects.filter(teams__slug=slug).distinct()
    return render(request, 'real_events/team.html', context_dict)

def all_members(request):
    context_dict = {}

    proff = request.GET.get("proff", "")
    if proff == "":
        context_dict['obj'] = Member.objects.all()
    else:
        obj = Member.objects.filter(professions__slug=proff).distinct()
        if obj.count() > 0:
            context_dict['obj'] = obj
        else:
            raise Http404("")
    return render(request, 'real_events/all_members.html', context_dict)
def member(request, slug):   
    context_dict = {}
    context_dict['obj'] = __get_model_by_slag(Member, slug)
    return render(request, 'real_events/member.html', context_dict)

def all_staff(request):
    context_dict = {}
    context_dict['obj'] = Staff.objects.all()
    return render(request, 'real_events/all_staff.html', context_dict)
def staff(request, slug):
    context_dict = {}
    context_dict['obj'] = __get_model_by_slag(Staff, slug)
    return render(request, 'real_events/staff.html', context_dict)


