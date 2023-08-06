import numpy as np
import trimesh
from compas.colors import Color
from compas.datastructures import Mesh
from compas.datastructures import Network
from compas.geometry import Shape
from compas.geometry import Primitive, Line, Polygon
from compas.geometry import centroid_points
from compas.utilities import pairwise
from typing import Union, Dict


class App(trimesh.Scene):

    def add(self, item, **kwargs):
        geometries = self.to_trimesh_geometries(item, **kwargs)
        for geometry in geometries:
            super().add_geometry(geometry)

    def convert_primitive(self, primitive: Primitive, **kwargs):
        if isinstance(primitive, Line):
            return self.convert_line(primitive, **kwargs)
        elif isinstance(primitive, Polygon):
            return self.convert_polygon(primitive, **kwargs)
        else:
            raise NotImplementedError

    def convert_line(self, line: Line, linecolor: Color = Color.black()):
        vertices = list(line)
        line = trimesh.path.entities.Line(points=[0, 1])
        path = trimesh.path.Path3D(vertices=vertices, entities=[line], process=False)
        path.colors = [linecolor]
        return [path]

    def convert_polygon(self, polygon: Polygon, **kwargs):
        mesh = Mesh.from_polygons([polygon])
        return self.convert_mesh(mesh, **kwargs)

    def convert_shape(self, shape: Shape, **kwargs):
        mesh = Mesh.from_shape(shape)
        return self.convert_mesh(mesh, **kwargs)

    def convert_network(self, network: Network,
                        pointcolor: Union[Dict[str, Color], Color] = Color.black(), linecolor: Union[Dict[str, Color], Color] = Color.grey(),
                        show_points: bool = True, show_lines: bool = True,
                        pointsize: float = 0.1):

        geometries = []

        vertices = []
        for node in network.nodes():
            vertices.append(network.node_attributes(node, 'xyz'))

        if show_lines:
            lines = []
            for v1, v2 in network.edges():
                line = trimesh.path.entities.Line(points=[v1, v2])
                lines.append(line)
            path = trimesh.path.Path3D(vertices=vertices, entities=lines, process=False)
            path.colors = [linecolor] * len(path.entities)
            geometries.append(path)

        if show_points:
            for vertex in vertices:
                sphere = trimesh.creation.uv_sphere(radius=pointsize)
                sphere.apply_translation(vertex)
                sphere.visual.vertex_colors = trimesh.visual.to_rgba(pointcolor)
                geometries.append(sphere)

        return geometries

    def convert_mesh(self, mesh: Mesh,
                     facecolor: Union[Dict[str, Color], Color] = Color.white(),
                     pointcolor: Union[Dict[str, Color], Color] = Color.black(),
                     linecolor: Union[Dict[str, Color], Color] = Color.grey(),
                     show_points: bool = False, show_lines: bool = True, show_faces: bool = True,
                     pointsize: float = 0.1):

        geometries = []

        vertices, faces = mesh.to_vertices_and_faces()
        if show_faces:

            if isinstance(facecolor, dict):
                facecolor = [facecolor[face] for face in mesh.faces()]
            else:
                facecolor = [facecolor for _ in mesh.faces()]

            tri_vertices = []
            tri_faces = []
            tri_face_colors = []
            vi = 0
            for i, face in enumerate(faces):
                if len(face) == 4:
                    tri_vertices.append(vertices[face[0]])
                    tri_vertices.append(vertices[face[1]])
                    tri_vertices.append(vertices[face[2]])
                    tri_vertices.append(vertices[face[2]])
                    tri_vertices.append(vertices[face[3]])
                    tri_vertices.append(vertices[face[0]])
                    tri_faces.append([vi, vi+1, vi+2])
                    tri_faces.append([vi+3, vi+4, vi+5])
                    tri_face_colors.append(facecolor[i])
                    tri_face_colors.append(facecolor[i])
                    vi += 6
                elif len(face) == 3:
                    tri_vertices.append(vertices[face[0]])
                    tri_vertices.append(vertices[face[1]])
                    tri_vertices.append(vertices[face[2]])
                    tri_faces.append([vi, vi+1, vi+2])
                    tri_face_colors.append(facecolor[i])
                    vi += 3
                elif len(face) > 4:
                    face_vertices = [vertices[v] for v in face]
                    c = centroid_points(face_vertices)
                    for a, b in pairwise(face_vertices + face_vertices[:1]):
                        tri_vertices.append(a)
                        tri_vertices.append(b)
                        tri_vertices.append(c)
                        tri_faces.append([vi, vi+1, vi+2])
                        tri_face_colors.append(facecolor[i])
                        vi += 3
                else:
                    raise ValueError('Invalid face length: {}'.format(len(face)))

            tri_face_colors += tri_face_colors
            tri_face_colors = trimesh.visual.to_rgba(tri_face_colors)
            tri_faces = np.array(tri_faces, dtype=int)
            tri_faces_backside = np.flip(tri_faces, axis=1)
            tri_faces = np.concatenate((tri_faces, tri_faces_backside), axis=0)
            _faces = trimesh.Trimesh(vertices=tri_vertices, faces=tri_faces, process=False)
            _faces.visual.face_colors = tri_face_colors

            geometries.append(_faces)

        if show_lines:
            vi = 0
            line_vertices = []
            lines = []
            if isinstance(linecolor, dict):
                pass
            else:
                linecolor = {edge: linecolor for edge in mesh.edges()}
            linecolors = []
            for v1, v2 in mesh.edges():
                linecolors.append(linecolor[(v1, v2)])
                v1 = mesh.vertex_attributes(v1, "xyz")
                v2 = mesh.vertex_attributes(v2, "xyz")
                line_vertices.append(v1)
                line_vertices.append(v2)
                line = trimesh.path.entities.Line(points=[vi, vi+1])
                lines.append(line)
                vi += 2
            path = trimesh.path.Path3D(vertices=line_vertices, entities=lines, process=False)
            path.colors = linecolors
            geometries.append(path)

        if show_points:
            if isinstance(pointcolor, dict):
                pass
            else:
                pointcolor = {vertex: pointcolor for vertex in mesh.vertices()}
            for vertex in mesh.vertices():
                xyz = mesh.vertex_attributes(vertex, "xyz")
                sphere = trimesh.creation.uv_sphere(radius=pointsize)
                sphere.apply_translation(xyz)
                sphere.visual.vertex_colors = trimesh.visual.to_rgba(pointcolor[vertex])
                geometries.append(sphere)

        return geometries

    def to_trimesh_geometries(self, item, **kwargs):

        if isinstance(item, Mesh):
            return self.convert_mesh(item, **kwargs)
        elif isinstance(item, Network):
            return self.convert_network(item, **kwargs)
        elif isinstance(item, Shape):
            return self.convert_shape(item, **kwargs)
        elif isinstance(item, Primitive):
            return self.convert_primitive(item, **kwargs)
        else:
            raise NotImplementedError
