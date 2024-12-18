from django.shortcuts import render, HttpResponse
from .models import Todolist
# Create your views here.
def home(request):
   person = [
    {"name": "Alice", "age": 15},
    {"name": "Bob", "age": 12},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 28},
    {"name": "Eve", "age": 35},
    {"name": "Frank", "age": 27},
    {"name": "Grace", "age": 24},
    {"name": "Hank", "age": 32},
    {"name": "Ivy", "age": 55},
    {"name": "Jack", "age": 26},
]

   context = {
      "name":"Diya",
      "persons":person
   }
   return render(request,'index.html',context)

def contact(request):
   return render(request,'contact.html',)


def todo(request):
   tasks = Todolist.objects.all()
   total_task = tasks.count()
   total_complete = tasks.filter(state = True).count()
   total_incomplete = tasks.filter(state = False).count()
   context = {
      "tasks":tasks,
      "total_task" : total_task,
      "total_complete" : total_complete,
      "total_incomplete" : total_incomplete
   }
   return render(request,'todolist.html', context)