# https://www.youtube.com/watch?v=xscQ9tcN4GI&list=PLa1F2ddGya_8acrgoQr1fTeIuQtkSd6BW&index=3


bl_info = {
    "name": "Add-on Name",
    "author": "Steponel",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "category": "Steponel",
    "location": "3D Viewport",
    "description": "Mass-import FBX files and keep track of where they came from",
    "warning": "",
    "doc_url": "https://space.bilibili.com/21077855",
    "tracker_url": "",
}

import bpy

# pathlib
# https://zhuanlan.zhihu.com/p/71861602
# http://c.biancheng.net/view/2541.html
import pathlib


# 获取文件夹路径
def mass_import_path(scene) -> pathlib.Path:
    abspath = bpy.path.abspath(scene.mass_import_path)
    return pathlib.Path(abspath)


class IMPORT_SCENE_OT_fbx_mass(bpy.types.Operator):
    bl_idname = "import_scene.fbx_mass"
    bl_label = "Mass-import FBXs"

    def execute(self, context):
        # Find the FBX files
        import_path = mass_import_path(context.scene)
        # For each file:
        #     - import it
        # 导入文件夹中所有FBX文件
        for import_fpath in import_path.glob("*.fbx"):
            bpy.ops.import_scene.fbx(filepath=str(import_fpath))
            #     - record its filename
            # 关联mass_import_fname属性，记录导入的FBX名称
            for imported_ob in context.selected_objects:
                imported_ob.mass_import_fname = import_fpath.name

        return {"FINISHED"}


class IMPORT_SCENE_OT_fbx_reload(bpy.types.Operator):
    bl_idname = "import_scene.fbx_reload"
    bl_label = "Reload import FBXs"

    def execute(self, context):
        ob = context.object

        # Store what we want to remember
        mass_import_fname = ob.mass_import_fname
        matrix_world = ob.matrix_world.copy()

        # Remove object from scene

        if ob.users == 0:
            bpy.data.objects.remove(ob)
        del ob

        # Load FBX file
        import_path = mass_import_path(context.scene)
        # import_fpath = 文件夹/fbx名称
        import_fpath = import_path / mass_import_fname
        bpy.ops.import_scene.fbx(filepath=str(import_fpath))
        # Restore What we remember
        for imported_ob in context.selected_objects:
            imported_ob.mass_import_fname = import_fpath.name
            imported_ob.matrix_world = matrix_world

        return {'FINISHED'}


class VIEW3D_PT_mass_import(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Monkeys"
    bl_label = "Mass Import"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        # show mass_import_path
        col.prop(context.scene, "mass_import_path")
        # IMPORT_SCENE_OT_fbx_mass
        col.operator("import_scene.fbx_mass")

        col = layout.column(align=True)
        if context.object:
            col.prop(context.object, "mass_import_fname")
            col.operator("import_scene.fbx_reload")
        else:
            col.label(text="-no active object-")


classes = [
    VIEW3D_PT_mass_import,
    IMPORT_SCENE_OT_fbx_mass,
    IMPORT_SCENE_OT_fbx_reload,
]


def register():
    # add a custom property of Scene
    bpy.types.Scene.mass_import_path = bpy.props.StringProperty(
        name="FBX Folder",
        # Subtype is Directory PATH
        subtype="DIR_PATH",
    )
    # add a custom property of Object
    bpy.types.Object.mass_import_fname = bpy.props.StringProperty(
        name="FBX File",
    )

    for cls in classes:
        bpy.utils.register_class(cls)
    # 添加到 菜单 View3D 中的 add mesh 中
    # bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw)


def unregister():
    del bpy.types.Scene.mass_import_path
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # 从中移除
    # bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw)


if __name__ == "__main__":
    register()
