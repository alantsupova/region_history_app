from rest_framework import serializers


class RouteListSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()

class PlacesSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()
    coordinate_x = serializers.CharField()
    coordinate_y  = serializers.CharField()


class RouteDetailSerializer(serializers.Serializer):
    title = serializers.CharField()
    time = serializers.CharField()
    places = PlacesSerializer(many=True)
