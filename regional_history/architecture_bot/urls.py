from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('route', views.RoutesViewSet, basename='route')

urlpatterns = [
    path('', include(router.urls)),
    path('closest-places/', views.ClosestPlaces.as_view(), name='closest-places'),
    path('closest-route/', views.ClosestRoute.as_view(), name='closest-route'),
    path('circle-route/', views.CircleRoute.as_view(), name='circle-route')
]
