# import bpy

# # 循环创建立方体
# for k in range(5):
#     for j in range(5):
#         for i in range(5):
#             bpy.ops.mesh.primitive_cube_add(size=0.25, location=[i, j, k])

#############################################

# # 选择、激活和规范 #
# # 选择对象
# def my_selector(objname, additive=False):
#     # 默认情况清除其他选择物体
#     if not additive:
#         bpy.ops.object.select_all(action='DESELECT')
#
#     # 选定objname
#     bpy.data.objects[objname].select_set(True)
#
#
# # 只选Cube
# my_selector('Cube')
# # 附加选Sphere
# my_selector('Sphere', additive=True)
# # 对选择物体变换
# bpy.ops.transform.translate(value=[1, 0, 0])

# # 激活对象
# def my_activator(objname):
#     # 视图层活跃物体为objname
#     bpy.context.view_layer.objects.active = bpy.data.objects[objname]
#
#
# my_activator('Sphere')
# # 选择活跃物体
# print("Selected objects:", bpy.context.active_object)

# # 指定对象（按名称访问）
# def my_specifier(objname):
#     return bpy.data.objects[objname]


# CHAPTER 3 The bmesh Module

# #更改编辑模式为EDIT
# bpy.ops.object.mode_set(mode='EDIT')
# #更改编辑模式为OBJECT
# bpy.ops.object.mode_set(mode='OBJECT')
#
# # 实例化bmesh对象
# import bmesh
#
# # 删除所有物体
# bpy.ops.object.mode_set(mode='OBJECT')  # 物体模式
# bpy.ops.object.select_all(action='SELECT')  # 选择所有
# bpy.ops.object.delete()  # 删除
# # 添加Cube进入编辑模式
# bpy.ops.mesh.primitive_cube_add(size=1, location=[0, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
# # 储存一个网格数据块引用
# mesh_datablock = bpy.context.object.data
# #
# bm = bmesh.from_edit_mesh(mesh_datablock)
#
# print(bm)

# 选择3D对象的各部分

# import bpy
# import bmesh
#
# # 删除所有的物体
# bpy.ops.object.mode_set(mode='OBJECT')
# bpy.ops.object.select_all(action='SELECT')
# bpy.ops.object.delete()
#
# # 创建一个Cube；进入Edit Mode
# bpy.ops.mesh.primitive_cube_add(size=1, location=[0, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
#
# # 选择模式改为面模式
# bpy.ops.mesh.select_mode(type='FACE')
# # 注册bmesh对象将选择部分纳入
# bm = bmesh.from_edit_mesh(bpy.context.object.data)
#
# # 选择一个面
# # 使用ensure_lookup_table 提醒Blender防止bmesh对象的某些部分在操作之间被垃圾收集。
# # 这些函数占用最小的处理能力，因此我们可以随意调用它们，而不会产生太多后果。过度调用它们比低估调用它们更好
# # 不调用可能出现此错误 ReferenceError: BMesh data of type BMesh has been removed
# bm.faces.ensure_lookup_table()
# bm.faces[0].select = True
#
# # 选择一个边edge
# bm.edges.ensure_lookup_table()
# bm.edges[7].select = True
#
# # 选择一个顶点
# bm.verts.ensure_lookup_table()
# bm.verts[5].select = True

#
# # 编辑模式下的变化
# import bpy
# import bmesh
#
# # 删除所有的物体
# bpy.ops.object.mode_set(mode='OBJECT')
# bpy.ops.object.select_all(action='SELECT')
# bpy.ops.object.delete()
#
# # 创建一个Cube；进入Edit Mode；弃选所有
# bpy.ops.mesh.primitive_cube_add(size=1, location=[-3, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='DESELECT')
#
# # 面模式
# bpy.ops.mesh.select_mode(type='FACE')
#
# # 定义bm，选择各部分
# bm = bmesh.from_edit_mesh(bpy.context.object.data)
# bm.faces.ensure_lookup_table()
# bm.faces[1].select = True
# # 按Y轴旋转
# bpy.ops.transform.rotate(value=0.3, orient_axis='Y')
#
# bpy.ops.object.mode_set(mode='OBJECT')
#
# # create a cube;沿y轴平移一条边
# bpy.ops.mesh.primitive_cube_add(size=0.5)
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='DESELECT')
#
# bm = bmesh.from_edit_mesh(bpy.context.object.data)
# bm.edges.ensure_lookup_table()
# bm.edges[4].select = True
# bpy.ops.transform.translate(value=[0, 0.5, 0])
#
# bpy.ops.object.mode_set(mode='OBJECT')
#
# # YZ平移一顶点
# bpy.ops.mesh.primitive_cube_add(size=0.5, location=[3, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='DESELECT')
#
# bm = bmesh.from_edit_mesh(bpy.context.object.data)
# bm.verts.ensure_lookup_table()
# bm.verts[3].select = True
# bpy.ops.transform.translate(value=[0, 1, 1])
#
# bpy.ops.object.mode_set(mode='OBJECT')


# # 高级转换
# import bpy
# import bmesh
# from pip._vendor.six import b
#
# bpy.ops.object.mode_set(mode='OBJECT')
# bpy.ops.object.select_all(action='SELECT')
# bpy.ops.object.delete()
#
# bpy.ops.mesh.primitive_cube_add(size=0.5, location=[-3, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='DESELECT')
#
# bpy.ops.mesh.select_mode(type='FACE')
#
# bm = bmesh.from_edit_mesh(bpy.context.object.data)
# bm.faces.ensure_lookup_table()
# bm.faces[5].select = True
#
# # 挤出区域 移动按法线方向
# bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={'value': [0.3, 0.3, 0.3],
#                                                          'constraint_axis': [True, True, True],
#                                                          'orient_matrix_type': 'NORMAL'})
#
# bpy.ops.object.mode_set(mode='OBJECT')
#
# bpy.ops.mesh.primitive_cube_add(size=0.5, location=[0, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='DESELECT')
#
# bm = bmesh.from_edit_mesh(bpy.context.object.data)
# bm.faces.ensure_lookup_table()
# bm.faces[5].select_set(True)
#
# # 选择面 细分操作
# bpy.ops.mesh.subdivide(number_cuts=2)
#
# bpy.ops.mesh.select_all(action='DESELECT')
# bm.faces.ensure_lookup_table()
# bm.faces[5].select = True
# bm.faces[7].select = True
# bpy.ops.transform.translate(value=[0, 0, 0.5])
#
# bpy.ops.object.mode_set(mode='OBJECT')
#
# bpy.ops.mesh.primitive_cube_add(size=0.5, location=[3, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='SELECT')
# # 顶点随机
# bpy.ops.transform.vertex_random(offset=0.5)
#
# bpy.ops.object.mode_set(mode='OBJECT')


# import bpy
#
# bpy.ops.object.modifier_add(type='EDGE_SPLIT')
# bpy.context.object.modifiers["EdgeSplit"].split_angle = 100
# bpy.ops.object.modifier_apply(modifier="EdgeSplit",report=True)
#



