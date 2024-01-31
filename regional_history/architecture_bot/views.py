from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, viewsets

from .models import Places, Routes
from .services import get_closest_places, get_simple_route, get_circle_route
from .serializers import RouteListSerializer, RouteDetailSerializer


class ClosestPlaces(APIView):
    """
    Получение ближайших мест

    Просто n близких к пользователю мест
    """
    def get(self, request):
        places = Places.objects.values()
        return Response(get_closest_places(request.query_params.get('coor_x'),
                                         request.query_params.get('coor_y'),
                                         list(places),
                                         int(request.query_params.get('amount'))))


class ClosestRoute(APIView):
    """
    Получение обычного маршрута (получаем блиажйшее место к пользователю, ближайшее к этому место и тд)
    """
    def get(self, request):
        places = Places.objects.values()
        return Response(get_simple_route(request.query_params.get('coor_x'),
                                         request.query_params.get('coor_y'),
                                         list(places),
                                         int(request.query_params.get('amount'))))


class CircleRoute(APIView):
    """
    Получение кругового маршрута
    """
    def get(self, request):
        places = Places.objects.values()
        return Response((get_circle_route(request.query_params.get('coordinate_x'),
                                         request.query_params.get('coordinate_x'),
                                         list(places),
                                         int(request.query_params.get('amount')))))


class RoutesViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Получение списка маршрутов и детальной информации о маршруте
    """
    queryset = Routes.objects.prefetch_related('places').all()
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RouteDetailSerializer
        elif self.action == 'list':
            return RouteListSerializer

