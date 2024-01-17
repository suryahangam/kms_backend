from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from user.views import (
    EmployeeRegistration, 
    LoginView,
    ProfileViewSet
    )

app_name = 'api'

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register', EmployeeRegistration.as_view(), name='employee_registration'),
    path('login', LoginView.as_view(), name='employee_login'),
    # path('logout'),\
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),


]
