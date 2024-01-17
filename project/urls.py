from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project.views import ProjectViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]
