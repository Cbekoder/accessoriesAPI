from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Accessories Warehouse API",
      default_version='v1',
      description="API documentation for the Accessories Magazine Warehouse System. Manage products, categories, and stock with ease.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="cbekoder@gmail.com"),
      license=openapi.License(name="Proprietary License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('inventory/', include('inventory.urls')),
    path('transaction/', include('main.urls')),
    path('dashboard/', include('main.urls_dashboard')),
]
