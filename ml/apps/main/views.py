from django.shortcuts import render, redirect

from .models import Exercise;
from .form import ExerciseForm;
# Create your views here.

def index(request):
    posters = Exercise.objects.all();
    context = {"title": "Creacion", 'posters': posters}
    return render(request, "main/index.html", context);

def create(request):
    posters = Exercise.objects.all();

    if request.method == 'GET':
        form = ExerciseForm;
        context = {"title": "Creacion", 'posters': posters, 'form' : form}
    else:
        form = ExerciseForm(request.POST);
        context = {"title": "Creacion", 'posters': posters, 'form' : form}
        if form.is_valid():
            form.save();
            return redirect("home");

    return render(request, "main/create.html", context);

def modify_delete(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        e_id = int(request.POST["num_exercise"]);
        exercise = Exercise.objects.get(id = e_id);
        print(exercise);

    if request.POST["choice"] == "1":
        redirect("modificar");
    else:
        exercise.delete();
        return redirect("home");


    context = {"title": "Modificar"}
    return render(request, "main/crud.html", context);
