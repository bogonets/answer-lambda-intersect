import sys
import os

import numpy as np

import shapely
from shapely.geometry import Polygon, LineString, Point
import intersect


point = 'top-left'


def on_set(k, v):
    if k == 'point':
        global point
        point = v


def on_get(k):
    if k == 'point':
        return point


def on_run(boxes, polygons):

    pts = intersect.get_point_of_box(boxes, point)

    intersect = intersect.intersect_points_with_polygons_with_index(pts, polygons)

    result = [boxes[i] for i in range(len(boxes)) if intersect[i]]
    remain = [boxes[i] for i in range(len(boxes)) if not intersect[i]]

    return {
        'intersect': np.array(result),
        'remain': np.array(remain)
    }


