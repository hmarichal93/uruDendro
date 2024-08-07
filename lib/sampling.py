"""
Copyright (c) 2023 Author(s) Henry Marichal (hmarichal93@gmail.com

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import numpy as np
from shapely.geometry import Point
from shapely.geometry.linestring import LineString


from .chain import Node, euclidean_distance, get_node_from_list_by_angle


class Ray(LineString):
    def __init__(self, direction, center, M, N):
        self.direction = direction
        self.border = self._image_border_radii_intersection(direction, center, M, N)
        super().__init__([center, self.border])

    @staticmethod
    def _image_border_radii_intersection(theta, origin, M, N):
        degree_to_radians = np.pi / 180
        theta = theta % 360
        yc, xc = origin
        if 0 <= theta < 45:
            ye = M - 1
            xe = np.tan(theta * degree_to_radians) * (M - 1 - yc) + xc

        elif 45 <= theta < 90:
            xe = N - 1
            ye = np.tan((90 - theta) * degree_to_radians) * (N - 1 - xc) + yc

        elif 90 <= theta < 135:
            xe = N - 1
            ye = yc - np.tan((theta - 90) * degree_to_radians) * (xe - xc)

        elif 135 <= theta < 180:
            ye = 0
            xe = np.tan((180 - theta) * degree_to_radians) * (yc) + xc

        elif 180 <= theta < 225:
            ye = 0
            xe = xc - np.tan((theta - 180) * degree_to_radians) * (yc)

        elif 225 <= theta < 270:
            xe = 0
            ye = yc - np.tan((270 - theta) * degree_to_radians) * (xc)

        elif 270 <= theta < 315:
            xe = 0
            ye = np.tan((theta - 270) * degree_to_radians) * (xc) + yc

        elif 315 <= theta < 360:
            ye = M - 1
            xe = xc - np.tan((360 - theta) * degree_to_radians) * (ye - yc)

        else:
            raise 'Error'

        return (ye, xe)


def build_rays(Nr, M, N, center):
    """

    @param Nr: total rays
    @param N: widht image
    @param M: height_output image
    @param center: (y,x)
    @return: list_position rays
    """
    angles_range = np.arange(0, 360, 360 / Nr)
    radii_list = [Ray(direction, center, M, N) for direction in angles_range]
    return radii_list


def get_coordinates_from_intersection(inter):
    """Shapely intersection formating"""
    if 'MULTI' in inter.wkt:
        inter = inter[0]

    if type(inter) == Point:
        y, x = inter.xy
        y,x = y[0], x[0]

    elif 'LINESTRING' in inter.wkt:
        y, x = inter.xy
        y,x = y[1], x[1]

    elif 'STRING' in inter.wkt:
        y, x = inter.coords.xy
        y,x = y[0], x[0]

    else:
        raise

    return y, x

from shapely.errors import TopologicalError

def compute_intersection(l_rays, curve, chain_id, center):
    """
    Compute intersection between rays and devernay curve
    @param l_rays: rays list
    @param curve: devernay curve
    @param chain_id: chain id
    @param center: disk image center
    @return: nodes list
    """
    ###shapely polygon validation
    if not curve.is_valid:
        curve = curve.buffer(0)
        if not curve.is_valid:
            raise ValueError('Invalid shapely polygon')

    ##########
    if curve.is_empty:
        raise

    l_curve_nodes = []
    for radii in l_rays:
        try:
            inter = radii.intersection(curve)
            if not inter.is_empty:
                y, x = get_coordinates_from_intersection(inter)
                i, j = np.array(y), np.array(x)
                params = {'y': i, 'x': j, 'angle': int(radii.direction), 'radial_distance':
                    euclidean_distance([i, j], center), 'chain_id': chain_id}
                dot = Node(**params)
                if dot not in l_curve_nodes and get_node_from_list_by_angle(l_curve_nodes, radii.direction) is None:
                    l_curve_nodes.append(dot)

            else:
                print('Empty intersection')


        except NotImplementedError:
            continue
        except TopologicalError:
            continue
    if len(l_curve_nodes) == 0:
        return None
    return l_curve_nodes

