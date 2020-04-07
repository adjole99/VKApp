from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseNotFound
from .models import user,Task,Advices
# Create your views here.

#Получение данных из бд
def index(request):
    user = user.object.all()
    return render(request,"index.html",{'user':user})

def create_user(request):
    if request.method == "POST":
     user1 = user()
     user1.user_name = request.POST.get("user_name")
     user1.user_taskList = request.POST.get("taskList")
     user1.user_adviceList = request.POST.get("adviceList")
     user1.task_achieved = request.POST.get("task_achieved")
     user1.save()
     return HttpResponseRedirect("/")

def create_task(request):
    if request.method == "POST":
     task1 = Task()
     task1.task_id = request.POST.get("task_id")
     task1.task_category = request.POST.get("task_category")
     task1.task_model = request.POST.get("task_model")
     task1.task_achieved = request.POST.get("task_achieved")
     task1.save()
     return HttpResponseRedirect("/")

def create_advice(request):
    if request.method == "POST":
     advice1 = Advices()
     advice1.advice_id = request.POST.get("advice_id")
     advice1.advice_category = request.POST.get("advice_category")
     advice1.advice_text = request.POST.get("advice_category")
     advice1.save()
     return HttpResponseRedirect("/")

# Изменение данных

def edit_user(request,id):
    try:
      user = user.objects.get(id = id)
      if request.method == "POST":
         user1 = user()
         user1.user_name = request.POST.get("user_name")
         user1.user_taskList = request.POST.get("taskList")
         user1.user_adviceList = request.POST.get("adviceList")
         user1.task_achieved = request.POST.get("task_achieved")
         user1.save()
         return HttpResponseRedirect("/")
      else:
          return render(request,"edit.html",{"user":user})
    except user.DoesNotExist:
        return HttpResponseNotFound("<h4>User not found</h4>")
def edit_advice(request,id):
    try:
        advice = advice.objects.get(id = id)
        if request.method == "POST":
             advice1 = Advices()
             advice1.advice_id = request.POST.get("advice_id")
             advice1.advice_category = request.POST.get("advice_category")
             advice1.advice_text = request.POST.get("advice_category")
             advice1.save()
             return HttpResponseRedirect("/")
        else:
            return render(request,"edit.html",{"advice":advice})
    except Advices.DoesNotExist:
        return HttpResponseNotFound("<h4>Advice does not exist</h4>")
def edit_task(request,id):
    try:
        advice = advice.objects.get(id=id)
        if request.method =="POST":
             task1 = Task()
             task1.task_id = request.POST.get("task_id")
             task1.task_category = request.POST.get("task_category")
             task1.task_model = request.POST.get("task_model")
             task1.task_achieved = request.POST.get("task_achieved")
             task1.save()
             return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h4>Task does not exist</h4>")

#Удаление из бд


def delete_advice(request,id):
    try:
        advice = Advices.objects.get(id=id)
        advice.delete()
        return HttpResponseRedirect("/")
    except Advices.DoesNotExist:
        return HttpResponseNotFound("<h5>Advice not found</h5>")

def delete_task(request,id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h5>Task not found <h5/>")