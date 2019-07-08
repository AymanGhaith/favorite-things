from django.urls import include, path
from rest_framework import routers
from favorit_things_app import views

router = routers.DefaultRouter()
router.register(r'favoriteThings', views.FavoriteThingViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'auditTrails',views.AuditTrailViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]