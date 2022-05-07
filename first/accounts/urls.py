from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import (RegisterViewSet,
                    LoginViewSet,
                    EditUserViewSet,
                    ConfirmViewSet)


urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'confirm', ConfirmViewSet, basename='confirm')
router.register(r'update', EditUserViewSet, basename='update')
urlpatterns += router.urls