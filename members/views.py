from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
    first = request.POST['first']
    level = request.POST['level']
    mood = request.POST['mood']
    reason = request.POST['reason']

    member = Members(name=first, level=level, mood=mood, reason=reason)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
  
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

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