from django.shortcuts import render, HttpResponse

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
   # return HttpResponse("Hello World")

def contact(request):
   return HttpResponse("This is contact page")

# aboutpage, welcome page create