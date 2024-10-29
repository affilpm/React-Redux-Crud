from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Create a router and register your viewset
# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [


    #  path('api/', include(router.urls)),
    
]
