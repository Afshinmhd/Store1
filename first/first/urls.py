"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('accounts/', include('blog.urls'))
"""
from django.contrib                         import admin
from django.urls                            import path, include, re_path
from rest_framework_simplejwt.views         import TokenRefreshView
from rest_framework.routers                 import DefaultRouter
from common.swagger                         import schema_view

from home.urls                              import router as home_router
from accounts.urls                          import router as accounts_router
from orders.urls                            import router as orders_router


router = DefaultRouter()
router.registry.extend(accounts_router.registry)
router.registry.extend(home_router.registry)
router.registry.extend(orders_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', include('home.urls')),
    path('orders/', include('orders.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
