from .models import *
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields = "__all__"

    def validate_cources(self,value):
        #add all cource which are important for same standard
        importand_cour = Courses.objects.filter(standard=self.initial_data["standard"],iscompulsory=True)
        for cour in importand_cour:
            if cour.id not in value:
                value.append(cour.id)
        return value

