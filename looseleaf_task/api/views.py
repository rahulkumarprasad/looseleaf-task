from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

#deceroater for configuring text of api
@method_decorator(name="list",decorator=swagger_auto_schema(operation_description='GET /api/students/, List all students.'))
@method_decorator(name="create",decorator=swagger_auto_schema(operation_description='POST /api/students/, Create new student.'))
@method_decorator(name="retrieve",decorator=swagger_auto_schema(operation_description='GET /api/students/{id}/, Get detail of one student.'))
@method_decorator(name="update",decorator=swagger_auto_schema(operation_description='PUT /api/students/{id}/, Update all fields of one student.'))
@method_decorator(name="partial_update",decorator=swagger_auto_schema(operation_description='PATCH /api/students/{id}/, Make update to some fields of one student.'))
@method_decorator(name="destroy",decorator=swagger_auto_schema(operation_description='DELETE /api/students/{id}/, Delete one student.'))
class Student(ModelViewSet):
    #configuring the modelviewset 
    serializer_class=StudentSerializer
    queryset=Students.objects.all()
    allowed_methods=["GET","POST","PUT","PATCH","DELETE"]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

#deceroater for configuring text of api
@method_decorator(name="list",decorator=swagger_auto_schema(operation_description='GET /api/student/, List all cources.'))
@method_decorator(name="create",decorator=swagger_auto_schema(operation_description='POST /api/cources/, Create new cource.'))
@method_decorator(name="retrieve",decorator=swagger_auto_schema(operation_description='GET /api/cources/{id}/, Get detail of one cource.'))
@method_decorator(name="update",decorator=swagger_auto_schema(operation_description='PUT /api/cources/{id}/, Update all fields of one cource.'))
@method_decorator(name="partial_update",decorator=swagger_auto_schema(operation_description='PATCH /api/cources/{id}/, Make update to some fields of one cource.'))
@method_decorator(name="destroy",decorator=swagger_auto_schema(operation_description='DELETE /api/cources/{id}/, Delete one cource.'))
class Cource(ModelViewSet):
    #configuring the modelviewset 
    serializer_class=CourseSerializer
    queryset=Courses.objects.all()
    allowed_methods=["GET","POST","PUT","PATCH","DELETE"]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
