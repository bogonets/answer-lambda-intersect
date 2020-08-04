import sys
import os

import numpy as np

import shapely
from shapely.geometry import Polygon, LineString, Point
import intersect


point_type = 'top-left'


def on_set(k, v):
    if k == 'point':
        global point_type
        point_type = v


def on_get(k):
    if k == 'point':
        return point_type


def on_run(boxes, polygons):
    # sys.stdout.write(f"[intersect_polygon_box.on_run] boxes    :{boxes}\n")
    # sys.stdout.write(f"[intersect_polygon_box.on_run] boxes.size : {boxes.size}\n")
    # sys.stdout.write(f"[intersect_polygon_box.on_run] polygons : {polygons}\n")
    # sys.stdout.write(f"[intersect_polygon_box.on_run] polygons.size : {polygons.size}\n")
    # sys.stdout.flush()

    if polygons.size < 3:
        return {
            'intersect': None,
            'remain': boxes
        }

    if boxes.size < 4:
        return {'intersect': None, 'remain': None}

    points = [intersect.get_point_of_box(x, point_type) for x in boxes]
    # sys.stdout.write(f"[intersect_polygon_box.on_run] point type: {point_type}\n")
    # sys.stdout.write(f"[intersect_polygon_box.on_run] points: {points}\n")
    # sys.stdout.flush()

    intersection = intersect.intersect_points_with_polygons_with_index(points, polygons)

    result = [boxes[i] for i in range(len(boxes)) if intersection[i]]
    remain = [boxes[i] for i in range(len(boxes)) if not intersection[i]]

    # sys.stdout.write(f"boxes {boxes}\n")
    # sys.stdout.write(f"[intersect_polygon_box.on_run] points: {points}\n")
    # sys.stdout.write(f"intersection {intersection}\n")
    # sys.stdout.write(f"[intersect_polygon_box.on_run] result: {result}\n")
    # sys.stdout.write(f"[intersect_polygon_box.on_run] remain: {remain}\n")
    # sys.stdout.flush()
    if result:
        return {
            'intersect': np.array(result),
            'remain': np.array(remain)
        }
    else:
        return {
            'intersect': None,
            'remain': np.array(remain)
        }


