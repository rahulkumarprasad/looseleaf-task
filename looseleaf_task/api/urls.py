from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import Student,Cource
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#creating router for DRF
router=DefaultRouter()
router.register("students",Student,basename="student")
router.register("cources",Cource,basename="cources")

urlpatterns=[
    path("",include(router.urls)),

    #Using default token generator to generate accesstoken and refreshtoken
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]