# with-statement-in-python : https://www.pythonforbeginners.com/files/with-statement-in-python

bl_info = {
    "name": "Asset Linking",
    "author": "Steponel",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "category": "Steponel",
    "location": "File > Import",
    "description": "",
    "warning": "",
    "doc_url": "https://space.bilibili.com/21077855",
    "tracker_url": "",
}


import json
import bpy


def link_to_scene(
    filepath: str,  # 文件路径
    prefix: str,  # Collection筛选前缀
    link_to: bpy.types.Collection,
    location_y: float,
):
    # Link into the blend file
    # https://docs.blender.org/api/current/bpy.types.BlendDataLibraries.html?highlight=blenddata#bpy.types.BlendDataLibraries.load
    with bpy.data.libraries.load(filepath, link=True) as (
        data_from,
        data_to,
    ):  # load a library .blend file ;data_from源文件，data_to导入的部分
        for name in data_from.collections:
            if not name.startswith(
                prefix
            ):  # startswith 用于检查字符串是否是以指定子字符串开头，返回bool https://www.runoob.com/python/att-string-startswith.html
                continue  # 跳出本次循环 https://www.runoob.com/python/python-continue-statement.html
            data_to.collections.append(name)  # 添加到

    # Instance into the scene
    location_x = 0
    step_x = 2.0
    for coll in data_to.collections:
        # Check whether own the object
        if coll.name in link_to.objects:
            continue
        empty = bpy.data.objects.new(coll.name, None)
        empty.instance_type = "COLLECTION"
        empty.instance_collection = coll
        link_to.objects.link(empty)

        empty.location.x = location_x
        location_x += step_x

        empty.location.y = location_y


def ensure_collection(scene, collection_name) -> bpy.types.Collection:
    """Ensure have the collection.if none ,create it"""
    # https://www.runoob.com/python/python-exceptions.html
    try:
        link_to = scene.collection.children[collection_name]
    except KeyError:  # 映射键没有的话
        link_to = bpy.data.collections.new(collection_name)
        scene.collection.children.link(link_to)
    return link_to


class IMPORT_SCENE_OT_from_json(bpy.types.Operator):
    bl_idname = "import_scene.from_json"
    bl_label = "Link assets from JSON file"

    def execute(self, context):
        json_fname = bpy.path.abspath("//assets.json")
        # With as : https://www.jianshu.com/p/c00df845323c
        with open(json_fname) as infile:  # 导入json文件
            link_info = json.load(infile)  # Json转化成字典

        location_y = 0
        step_y = 2.0
        json_colls = link_info["collections"]
        for (
            coll_name,
            coll_info,
        ) in json_colls.items():  # dict.items()返回可遍历的(键, 值) 元组数组。
            link_to = ensure_collection(
                context, coll_name
            )  # ensure have the collection

            # 对应json数据循环
            for file_and_prefix in coll_info["link"]:
                filepath = file_and_prefix["file"]
                prefix = file_and_prefix["prefix"]
                link_to_scene(filepath, prefix, link_to, location_y)  # 每个file成一行

                location_y += step_y

        return {"FINISHED"}


def menu_func_import(self, context):
    self.layout.operator(IMPORT_SCENE_OT_from_json.bl_idname)


blender_classes = [
    IMPORT_SCENE_OT_from_json,
]


def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)  # 添加到导入菜单


def unregister():
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


# import bpy


# filepath = "D:\BlenderAddonsLearning\scripting_for_artists\Monkey.blend"  # https://blog.csdn.net/Anne332/article/details/107200119
# prefix = "M_"  # Collection筛选前缀

# # https://docs.blender.org/api/current/bpy.types.BlendDataLibraries.html?highlight=blenddata#bpy.types.BlendDataLibraries.load
# with bpy.data.libraries.load(filepath, link=True) as (
#     data_from,
#     data_to,
# ):  # load a library .blend file ;data_from源文件，data_to导入的部分
#     for coll_name in data_from.collections:
#         if not coll_name.startswith(
#             prefix
#         ):  # 用于检查字符串是否是以指定子字符串开头，返回bool https://www.runoob.com/python/att-string-startswith.html
#             continue  # 跳出本次循环 https://www.runoob.com/python/python-continue-statement.html
#         data_to.collections.append(coll_name)  # 导入

# scene = bpy.context.scene
# link_to_name = "Environment"
# # https://www.runoob.com/python/python-exceptions.html
# try:
#     link_to = scene.collection.children[link_to_name]
# except KeyError:  # 映射键没有的话
#     link_to = bpy.data.collections.new(link_to_name)
#     scene.collection.children.link(link_to)

# location_x = 0
# step_x = 2.0

# for coll in data_to.collections:
#     empty = bpy.data.objects.new(coll.name, None)
#     empty.instance_type = "COLLECTION"  # 设置实例化类型
#     empty.instance_collection = coll
#     link_to.objects.link(empty)  # Add to a collection

#     # 排列
#     empty.location.x = location_x
#     location_x += step_x


# import json
#
# import bpy
#
#
# def link_to_scene(
#         filepath: str,
#         prefix: str,
#         link_to: bpy.types.Collection,
#         location_y: float,
# ):
#     # Link into the blend file
#     with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to):
#         for name in data_from.collections:
#             if not name.startswith(prefix):
#                 continue
#             data_to.collections.append(name)
#
#     # Instance into the scene
#     location_x = 0
#     step_x = 2.0
#     for coll in data_to.collections:
#         if coll.name in link_to.objects:
#             continue
#         empty = bpy.data.objects.new(coll.name, None)
#         empty.instance_type = 'COLLECTION'
#         empty.instance_collection = coll
#         link_to.objects.link(empty)
#
#         empty.location.x = location_x
#         empty.location.y = location_y
#         location_x += step_x
#
#
# def ensure_collection(scene, collection_name) -> bpy.types.Collection:
#     try:
#         link_to = scene.collection.children[collection_name]
#     except KeyError:
#         link_to = bpy.data.collections.new(collection_name)
#         scene.collection.children.link(link_to)
#     return link_to
#
#
# class IMPORT_SCENE_OT_from_json(bpy.types.Operator):
#     bl_idname = 'import_scene.from_json'
#     bl_label = "Link assets from JSON file"
#
#     def execute(self, context):
#         json_fname = bpy.path.abspath('//assets.json')
#         with open(json_fname) as infile:
#             link_info = json.load(infile)
#
#         location_y = 0
#         step_y = 2.0
#         json_colls = link_info['collections']
#         for coll_name, coll_info in json_colls.items():
#             link_to = ensure_collection(context, coll_name)
#
#             for file_and_prefix in coll_info['link']:
#                 filepath = file_and_prefix['file']
#                 prefix = file_and_prefix['prefix']
#                 link_to_scene(filepath, prefix, link_to, location_y)
#
#                 location_y += step_y
#
#         return {'FINISHED'}
#
#
# def menu_func_import(self, context):
#     self.layout.operator(IMPORT_SCENE_OT_from_json.bl_idname)
#
#
# blender_classes = [
#     IMPORT_SCENE_OT_from_json,
# ]
#
#
# def register():
#     for blender_class in blender_classes:
#         bpy.utils.register_class(blender_class)
#     bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
#
#
# def unregister():
#     for blender_class in blender_classes:
#         bpy.utils.unregister_class(blender_class)
#     bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
