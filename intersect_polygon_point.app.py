import sys
import os

import numpy as np
from shapely.geometry import Polygon, LineString, Point



def on_run(points, polygons):
    list_point = []

    x = points[:,0]
    y = points[:,0]

    x = x.reshape(-1,1)
    y = y.reshape(-1,1)

    ppoints = np.append(x,y, axis=1)


    sys.stdout.write(f"intersect polygons~~~~{polygons}")
    sys.stdout.flush()



    for i in ppoints:
        for j in polygons:
            list_point.append(Point(i).intersects(Polygon(j)))
    
    sys.stdout.write(f"intersect~~~~{list_point}")
    sys.stdout.flush()

    intersect = np.array(list_point)

    return {
        'intersect' : intersect
    }

