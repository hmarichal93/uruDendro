"""
Copyright (c) 2023 Author(s) Henry Marichal (hmarichal93@gmail.com

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import numpy as np


def euclidean_distance(pix1, pix2):
    return np.sqrt((pix1[0] - pix2[0]) ** 2 + (pix1[1] - pix2[1]) ** 2)


def get_node_from_list_by_angle(dot_list, angle):
    try:
        dot = next(dot for dot in dot_list if (dot.angle == angle))
    except StopIteration as e:
        dot = None
    return dot


def get_chain_from_list_by_id(chain_list, chain_id):
    try:
        chain_in_list = next(chain for chain in chain_list if (chain.id == chain_id))

    except StopIteration:
        chain_in_list = None
    return chain_in_list


########################################################################################################################
# Class Node
########################################################################################################################
class Node:
    def __init__(self, x, y, chain_id, radial_distance, angle):
        self.x = x
        self.y = y
        self.chain_id = chain_id
        self.radial_distance = radial_distance
        self.angle = angle

    def __repr__(self):
        return (f'({self.x},{self.y}) ang:{self.angle} radio:{self.radial_distance:0.2f} cad.id {self.chain_id}\n')

    def __str__(self):
        return (f'({self.x},{self.y}) ang:{self.angle} radio:{self.radial_distance:0.2f} id {self.chain_id}')

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.angle == other.angle


def euclidean_distance_between_nodes(d1: Node, d2: Node):
    v1 = np.array([d1.x, d1.y], dtype=float)
    v2 = np.array([d2.x, d2.y], dtype=float)
    return euclidean_distance(v1, v2)


def copy_node(node: Node):
    return Node(**{'y': node.y, 'x': node.x, 'angle': node.angle, 'radial_distance':
        node.radial_distance, 'chain_id': node.chain_id})

