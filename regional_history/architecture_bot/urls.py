from django.urls import path

from . import views

urlpatterns = [
    path('closest-places', views.ClosestPlaces.as_view(), name='closest-places'),
    path('closest-route', views.ClosestRoute.as_view(), name='closest-route'),
    path('circle-route', views.CircleRoute.as_view(), name='circle-route')
]
