from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NameViewSet

router = DefaultRouter()
router.register(r'names', NameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.name_create, name='name_create'),
    path('<int:id>/', views.name_detail, name='name_detail'),
    path('<int:id>/edit/', views.name_edit, name='name_edit'),
    path('<int:id>/delete/', views.name_delete, name='name_delete'),
]
