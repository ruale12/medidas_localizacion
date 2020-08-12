from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField("nombre del ejericico", max_length = 30);
    description = models.TextField("description");
    pub_date = models.DateField("fecha creacion", auto_now = False, auto_now_add = True);
    out_date = models.DateField("fecha actualizacion", auto_now = True, auto_now_add = False);
    median = models.FloatField("guarda la media", default = 0.0);
    mean = models.FloatField("guarda la mediana", default = 0.0);
    mode = models.FloatField("guarda la moda", default = 0.0);
    trimmed_mean = models.FloatField("guarda media recortada", default = 0.0);
    trim_percentage = models.IntegerField("guarda el pocentaje media recortada");


    def __str__(self):
        return "{}:{}".format(self.id, self.name);


class Data(models.Model):
    excercise = models.ForeignKey(Exercise, on_delete=models.CASCADE);
    data = models.FloatField("guarda el dato");
    date = models.DateField("fecha actualizacion", auto_now = False, auto_now_add = True, null= True);

    def __str__(self):
        return "{}".format(self.data);
