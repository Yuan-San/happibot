from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('logs/', views.logs, name='logs'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  path('student/', views.student, name='student'),
  path('contact/', views.contact, name='contact'),
  path('student/show/<str:name>', views.deletemember, name='deletemember'),
  path('deletemember/memberdeleterequest/<int:id>', views.memberdeleterequest, name='memberdeleterequest')
]