"""looseleaf_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import urls as api_url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.clickjacking import xframe_options_sameorigin

#swager configration 
schema_view = get_schema_view(
   openapi.Info(
      title="Student API",
      default_version='1',
      description="This Api is used for Assigning cource to student, and also updating, deleteing, viewing Student and Cources.<h4 style='font-weight:400;'>For testing Api please visite <a href='/swagger/' target='_blank'>Test Api</a></h4>",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email=settings.EMAIL_ADDRESS),
    #  license=openapi.License(name="BSD"),
   ),
   public=True,
   
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url)),
  
    #swager
    path('swagger/', xframe_options_sameorigin(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
