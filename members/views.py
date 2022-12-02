from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  mymembers = Members.objects.all().values()
  happy = Members.objects.raw('SELECT 1 id, COUNT(mood) AS moodcount, mood FROM members_members GROUP BY mood ORDER BY moodcount desc;')
  total = Members.objects.raw('SELECT 1 id, COUNT(*) AS total FROM members_members;')
  """
  sad = Members.objects.raw('SELECT 1 id, COUNT(mood) AS moodcount, mood FROM members_members WHERE mood = Sad GROUP BY mood;')
  neutral = Members.objects.raw('SELECT 1 id, COUNT(mood) AS moodcount, mood FROM members_members WHERE mood = Neutral GROUP BY mood;')
  surprised = Members.objects.raw('SELECT 1 id, COUNT(mood) AS moodcount, mood FROM members_members WHERE mood = Surprised GROUP BY mood;')
  scared = Members.objects.raw('SELECT 1 id, COUNT(mood) AS moodcount, mood FROM members_members WHERE mood = Scared GROUP BY mood;')
  disgust = Members.objects.raw('SELECT 1 id, COUNT(mood) AS moodcount, mood FROM members_members WHERE mood = Disgust GROUP BY mood;')
  anger = Members.objects.raw('SELECT 1 id, COUNT(mood) AS moodcount, mood FROM members_members WHERE mood = Angry GROUP BY mood;')"""
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
    'happy': happy,
    'total': total,
  }
  """'sad': sad,
    'neutral': neutral,
    'surprised': surprised,
    'scared': scared,
    'disgust': disgust,
    'anger': anger"""
  return HttpResponse(template.render(context, request))

@login_required
def logs(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('logs.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
@login_required
def contact(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('reportissue.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

@login_required
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

@login_required
def student(request):
  mymembers = Members.objects.all().values()
  studentcount = Members.objects.raw('SELECT 1 id, name, COUNT(name) AS count, level, mood, reason FROM members_members GROUP BY name ORDER BY name asc;')
  template = loader.get_template('student.html')
  context = {
    'mymembers': mymembers,
    'studentcount': studentcount
  }
  return HttpResponse(template.render(context, request))

@login_required
def addrecord(request):
    first = request.POST['first']
    level = request.POST['level']
    mood = request.POST['mood']
    reason = request.POST['reason']
    member = Members(name=first, level=level, mood=mood, reason=reason)
    member.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def deletemember(request, name):
    membername = request.session.get('membername')
    logs = Members.objects.raw('SELECT id, name, mood, reason FROM members_members WHERE name = %s',[name])
    myname = Members.objects.raw('SELECT id, name, COUNT(name) AS namecount, level FROM members_members WHERE name = %s GROUP BY name', [name])
    membername = name
    request.session['membername'] = membername
    template = loader.get_template('eachstudent.html')
    context = {
      'logs':logs,
      'myname':myname
    }
    return HttpResponse(template.render(context, request))

@login_required
def memberdeleterequest(request, id):
    membername = request.session.get('membername')
    member = Members.objects.get(id=id)
    member.delete()
    url = reverse('deletemember', kwargs={'name': membername})
    return HttpResponseRedirect(url)

@login_required
def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

@login_required
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required
def updaterecord(request, id):
  first = request.POST['first']
  level = request.POST['level']
  mood = request.POST['mood']
  reason = request.POST['reason']
  member = Members.objects.get(id=id)
  member.name = first
  member.level = level
  member.mood = mood
  member.reason = reason
  member.save()
  return HttpResponseRedirect(reverse('index'))