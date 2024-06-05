from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NameViewSet

router = DefaultRouter()
router.register(r'api', NameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
