from geopy.distance import geodesic
from .tsp import tsp


def get_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    return geodesic((lat1, lon1), (lat2, lon2)).km


def get_closest_places(coor_x: float, coor_y: float, places: list, amount: int) -> list:
    closest_places = []
    for i in range(amount):
        closest_place = None
        closest_distance = float('inf')
        for place in places:
            distance = get_distance(coor_x, coor_y, float(place['coordinate_x']), float(place['coordinate_y']))
            if distance < closest_distance and place not in closest_places:
                closest_place = place
                closest_distance = distance
        if closest_place:
            closest_places.append(closest_place)
    return closest_places


def get_simple_route(coor_x: float, coor_y: float, places: list, amount: int) -> list:
    closest_places = []
    closest_place = None
    closest_distance = float('inf')
    for place in places:
        distance = get_distance(coor_x, coor_y, float(place['coordinate_x']),
                                    float(place['coordinate_y']))
        if distance < closest_distance and place not in closest_places:
            closest_place = place
            closest_distance = distance
    if closest_place:
        closest_places.append(closest_place)
    for i in range(amount - 1):
        closest_place = None
        closest_distance = float('inf')
        for place in places:
            distance = get_distance(places[-1]['coordinate_x'], places[-1]['coordinate_y'],
                                    float(place['coordinate_x']), float(place['coordinate_y']))
            if distance < closest_distance and place not in closest_places:
                closest_place = place
                closest_distance = distance
        if closest_place:
            closest_places.append(closest_place)
    return closest_places


def get_circle_route(coor_x: float, coor_y: float, places: list, amount: int) -> list:
    closest_places = [{'coordinate_x': coor_x, 'coordinate_y': coor_y}]
    for i in range(amount):
        closest_place = None
        closest_distance = float('inf')
        for place in places:
            distance = get_distance(coor_x, coor_y, float(place['coordinate_x']), float(place['coordinate_y']))
            if distance < closest_distance and place not in closest_places:
                closest_place = place
                closest_distance = distance
        if closest_place:
            closest_places.append(closest_place)
    order, route = tsp(closest_places)
    res = list()
    for o in order:
        res.append(closest_places[o])
    return res
