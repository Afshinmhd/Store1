from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from drf_yasg.inspectors import SwaggerAutoSchema


schema_view = get_schema_view(
   openapi.Info(
      title="Store APIS",
      default_version='v1',
      
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)