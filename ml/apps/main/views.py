from django.shortcuts import render, redirect

from .models import Exercise;
from .form import ExerciseForm;
# Create your views here.

def index(request):
    posters = Exercise.objects.all();
    context = {"title" : "Home", 'posters' : posters}
    return render(request, "main/index.html", context);

def create(request):
    posters = Exercise.objects.all();

    if request.method == 'GET':
        form = ExerciseForm;
        context = {"title": "Creacion", "pagina" : "/creacion/" ,"messageSubmit" : "Crear", 'posters': posters, 'form' : form}
    elif request.method == 'POST':
        form = ExerciseForm(request.POST);
        context = {"title": "Creacion", "pagina" : "/creacion/", "messageSubmit" : "Crear", 'posters': posters, 'form' : form}
        if form.is_valid():
            form.save();
            return redirect("home");

    return render(request, "main/create.html", context);

def modify_delete(request):
    # I want to use a same page to do Delete and Modify;
    if request.method == 'GET':
        exercise = Exercise.objects.all();
        return redirect("home");
    elif request.method == 'POST':
        e_id = int(request.POST["num_exercise"]);
        exercise = Exercise.objects.get(id = e_id);
        ## print(exercise);
        if request.POST["choice"] == "1":
            form = ExerciseForm(instance = exercise);
        else:
            exercise.delete();
            return redirect("home");


    context = {"title": "Modificar", "pagina" : "/modificarlist/", "messageSubmit" : "Modificar", "form" : form, "id" : e_id}
    return render(request, "main/create.html", context);

def modify(request):
    if request.method == "GET":
        context = {"title": "Lista Modificar", "messageSubmit" : "Modificar"}
    elif request.method == 'POST':
        e_id = int(request.POST["num"]);
        exercise = Exercise.objects.get(id = e_id);
        form = ExerciseForm(request.POST, instance = exercise);
        context = {"title": "Lista Modificar", "messageSubmit" : "Modificar"}
        if form.is_valid():
            form.save();
            return redirect("home");


    return render(request, "main/listar.html", context);

def delete(request):
    context = {"title": "Lista Eliminar", "messageSubmit" : "Modificar"}
    return render(request, "main/listar.html", context);
