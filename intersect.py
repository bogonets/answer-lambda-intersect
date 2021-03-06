import sys
import numpy as np
from shapely.geometry import Polygon, LineString, Point


LEFT_INDEX_OF_BOX = 0
TOP_INDEX_OF_BOX = 1
RIGHT_INDEX_OF_BOX = 2
BOTTOM_INDEX_OF_BOX = 3


def intersect_points_with_polygons_with_index(points, polygons):

    # sys.stdout.write(f"point {points}\n")
    # sys.stdout.write(f"poly {polygons}\n")
    # sys.stdout.flush()
    if isinstance(polygons, list):
        polygons = np.array(polygons)

    if len(polygons.shape) == 2:
        polygons = [Polygon(np.array(x).reshape(-1, 2).tolist())
                    for x in polygons]
    elif len(polygons.shape) == 3 and polygons.shape[0] == 2:
        polygons = [Polygon(x) for x in polygons]
    else:
        raise ValueError("Polygons's shape should be (-1, x) or (x).")

    points = [Point(x) for x in points]

    # sys.stdout.write(f"points {points}\n")
    # sys.stdout.flush()

    intersects = [pt if max([x.contains(pt) for x in polygons]) else [] for pt in points]

    return intersects


def intersect_points_with_polygons(points, polygons):
    intersects = intersect_points_with_polygons_with_index(points, polygons)
    return [x for x in intersects if x]


# def intersect_point_of_boxes_with_polygons(boxes, polygons, point_of_boxes):


def get_point_of_box(box, location):
    def get_w_center(b):
        return ((b[RIGHT_INDEX_OF_BOX] - b[LEFT_INDEX_OF_BOX]) / 2) + b[LEFT_INDEX_OF_BOX]

    def get_h_center(b):
        return ((b[BOTTOM_INDEX_OF_BOX] - b[TOP_INDEX_OF_BOX]) / 2) + b[TOP_INDEX_OF_BOX]

    if location == 'top-left':
        point = [box[LEFT_INDEX_OF_BOX], box[TOP_INDEX_OF_BOX]]
    elif location == 'top':
        point = [get_w_center(box), box[TOP_INDEX_OF_BOX]]
    elif location == 'top-right':
        point = [box[RIGHT_INDEX_OF_BOX], box[TOP_INDEX_OF_BOX]]
    elif location == 'left':
        point = [box[LEFT_INDEX_OF_BOX], get_h_center(box)]
    elif location == 'right':
        point = [box[RIGHT_INDEX_OF_BOX], get_h_center(box)]
    elif location == 'bottom-left':
        point = [box[LEFT_INDEX_OF_BOX], box[BOTTOM_INDEX_OF_BOX]]
    elif location == 'bottom':
        point = [get_w_center(box), box[BOTTOM_INDEX_OF_BOX]]
    elif location == 'bottom-right':
        point = [box[RIGHT_INDEX_OF_BOX], box[BOTTOM_INDEX_OF_BOX]]
    else:
        # elif location == 'center':
        point = [get_w_center(box), get_h_center(box)]
    return point
