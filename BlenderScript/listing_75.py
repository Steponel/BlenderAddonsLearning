# 使用硬编码Python变量
import bpy

# 清场
# bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Creat the lists of vertex and face data
my_vertexs = [(1.0, 1.0, -1.0),
              (1.0, -1.0, -1.0),
              (-1.0, -1.0, -1.0),
              (-1.0, 1.0, -1.0),
              (1.0, 1.0, 1.0),
              (1.0, -1.0, 1.0),
              (-1.0, -1.0, 1.0),
              (-1.0, 1.0, 1.0)]
# my_edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
my_faces = [(0, 1, 2, 3),
            (4, 7, 6, 5),
            (0, 4, 5, 1),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (4, 0, 3, 7)]

# Create a mesh use from_pydata() and bpy.data.objects.new()
mesh_data = bpy.data.meshes.new("cube_mesh_data")
mesh_data.from_pydata(my_vertexs, [], my_faces)
mesh_data.update()

my_object = bpy.data.objects.new("MyObject", mesh_data)

scene = bpy.context.scene
scene.collection.objects.link(my_object)
my_object.select_set(state=True)
