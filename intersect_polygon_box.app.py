import sys
import os

import numpy as np

import shapely
from shapely.geometry import Polygon, LineString, Point
import intersect


# boxes [[xmin, ymin, xmax, ymax, score, class], ...]
# polygons [[x1,y1, x2,y2, x3,y3, ...], ...]

a = np.array([[500, 500, 550, 550, 0.9, 1], [100, 100, 150, 150, 0.9, 1]])
p = np.array([[300, 300, 700, 300, 700, 700, 300, 700],
              [300, 300, 700, 300, 700, 700, 300, 700]])


def test(boxs, polygons):
    a = boxs[0:, 0:2]
    a = a.reshape(-1, 2).tolist()
    print(a)
    return
    # a1 = Point(a[0,0:2].tolist())
    # a2 = Point(a[1,0:2].tolist())
    # points = [a1, a2]
    # print(points)

    #[[300, 300], [700, 300], [700,700], [300, 700]]
    polys = Polygon(p.reshape(-1, 2).tolist())
    print(polys)

    intersects = []
    for idx, pt in enumerate(points):
        if polys.intersects(pt):
            print(type(intersects.append(idx)))

    result = [a[x] for x in intersects]
    result = np.array(result)

    sys.stdout.write(f"intersect polygons~~~~{result}\n")
    sys.stdout.flush()

    assert(result.tolist() == r.tolist())


if __name__ == "__main__":
    test(a, p)



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

    return {
        'intersect': np.array(result)
    }


