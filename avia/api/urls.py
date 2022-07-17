from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.views import (
    AirportViewSet,
    CompanyViewSet,
    Pass_in_tripViewSet,
    PlaneViewSet,
    TripViewSet
)

schema_view = get_schema_view(
   openapi.Info(
      title="Avia API",
      default_version='v1',
      description="Документация для приложения api проекта Avia",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="ee@ya.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'api'
router_v1 = DefaultRouter()
router_v1.register('trip', TripViewSet, 'trip')
router_v1.register('pass_in_trip', Pass_in_tripViewSet, 'pass_in_trip')
router_v1.register('airport', AirportViewSet, 'airport')
router_v1.register('plane', PlaneViewSet, 'plane')
router_v1.register('company', CompanyViewSet, 'company')

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/', include(router_v1.urls)),
]

# urlpatterns += [
#     url(r'^swagger(?P<format>\.json|\.yaml)$', 
#         schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
#         name='schema-swagger-ui'),
#     url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
#         name='schema-redoc'),
# ] 
