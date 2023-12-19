from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Places
from .services import get_closest_places, get_simple_route, get_circle_route


class ClosestPlaces(APIView):
    """
    Получение ближайших мест

    Просто n близких к пользователю мест
    """
    def get(self, request):
        places = Places.objects.values()
        data = request.data()
        return Response(get_closest_places(data['coor_x'], data['coor_y'], places, data['amount']))


class ClosestRoute(APIView):
    """
    Получение обычного маршрута (получаем блиажйшее место к пользователю, ближайшее к этому место и тд)
    """
    def get(self, request):
        places = Places.objects.values()
        data = request.data()
        return Response(get_simple_route(data['coor_x'], data['coor_y'], places, data['amount']))


class CircleRoute(APIView):
    """
    Получение кругового маршрута
    """
    def get(self, request):
        places = Places.objects.values()
        data = request.data()
        return Response(get_circle_route(data['coor_x'], data['coor_y'], places, data['amount']))

