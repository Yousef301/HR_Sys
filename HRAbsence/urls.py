from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('user', UserView, basename="user")
register = DefaultRouter()
register.register('register', RegisterView, basename="register")
absence = DefaultRouter()
absence.register('absence', AbsenceView, basename="absence")
business = DefaultRouter()
business.register('business', BusinessView, basename="business")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(register.urls)),
    path('', include(absence.urls)),
    path('', include(business.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]