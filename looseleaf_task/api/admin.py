from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display=["course_name","standard","iscompulsory"]

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","standard","all_cource"]

    def all_cource(self,obj):
        '''For displaying all the cources selected'''
        all_data=""
        for i,cour in enumerate(obj.cources.all()):
            all_data += cour.course_name+(", " if i < obj.cources.all().count()-1 else "" )
        if all_data.strip() == "":
            all_data="------"
        return all_data

    def save_model(self, request, obj, form, change):
        '''method to auto assign important subject to the user'''
        #filtering the queryset to make sure that other standard subject does not asigne
        obj.cources.set(form.cleaned_data['cources'].filter(standard=obj.standard))
        importand_cour = Courses.objects.filter(standard=obj.standard,iscompulsory=True)
        for cour in importand_cour:
            obj.cources.add(cour)
        form.cleaned_data['cources']=obj.cources.all()
        obj.save()
        super(StudentsAdmin,self).save_model(request, obj, form, change)
        
