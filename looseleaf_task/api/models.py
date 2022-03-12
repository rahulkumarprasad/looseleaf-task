from django.db import models

class Courses(models.Model):
    course_name=models.CharField(max_length=500)
    standard=models.CharField(max_length=500)
    iscompulsory=models.BooleanField(default=True)

    def __str__(self):
        return self.course_name +" ("+ ("important" if self.iscompulsory == True else "elective")+")"

class Students(models.Model):
    first_name=models.CharField(max_length=500)
    last_name=models.CharField(max_length=500)
    standard=models.IntegerField()
    cources=models.ManyToManyField(Courses,blank=True,null=True)

    def __str__(self):
        return self.first_name +" "+ self.last_name