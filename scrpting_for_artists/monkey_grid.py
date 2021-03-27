# https://www.youtube.com/watch?v=xscQ9tcN4GI&list=PLa1F2ddGya_8acrgoQr1fTeIuQtkSd6BW&index=3


bl_info = {
    "name": "Add-on Name",
    "author": "Steponel",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "category": "Steponel",
    "location": "Where can we use it?",
    "description": "",
    "warning": "",
    "doc_url": "https://space.bilibili.com/21077855",
    "tracker_url": "",
}
# VScode: Ctrl F2 当前文件批量重命名

import bpy


class MESH_OT_monkey_grid(bpy.types.Operator):
    """Let's spread some joy"""

    bl_idname = "mesh.monkey_grid"
    bl_label = "Monkey Grid"
    bl_options = {"REGISTER", "UNDO"}

    count_x: bpy.props.IntProperty(
        name="X",
        description="Number of Monkey in the X-direction",
        default=3,
        min=1,
        max=10,
    )
    count_y: bpy.props.IntProperty(
        name="Y",
        description="Number of Monkey in the Y-direction",
        default=4,
        min=1,
        max=10,
    )
    size: bpy.props.FloatProperty(
        name="size", description="Size of Monkey", default=1, min=0, max=1
    )

    # bpy_learning\ApplicationModules\types\operator\Note.md

    @classmethod
    def poll(cls, context):
        print(f"My area is:{context.area.type}")
        # 只能在3d界面使用
        return bpy.context.area.type == "VIEW_3D"

    def execute(self, context):
        for idx in range(self.count_x * self.count_y):
            # % fmod
            # // Floor
            # 方阵排列猴子
            x = idx % self.count_x
            y = idx // self.count_x
            bpy.ops.mesh.primitive_monkey_add(size=self.size, location=(x, y, 1))

        return {"FINISHED"}


class VIEW3D_PT_monkey_grid(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Monkeys"
    bl_label = "Grid"


    def draw(self, context):
        col = self.layout.column(align=True)
        self.layout.operator(
            operator="mesh.monkey_grid", text="Default Grid", icon="MONKEY"
        )
        # 面板显示操作符按钮，并更改了操作符默认值
        props = self.layout.operator(
            operator="mesh.monkey_grid", text="BigGrid", icon="MONKEY"
        )
        props.count_x = 10
        props.count_y = 10
        props.size = 0.8

        # 面板显示操作符按钮，并更改了操作符默认值
        props = self.layout.operator(
            operator="mesh.monkey_grid", text="SmallGrid", icon="MONKEY"
        )
        props.count_x = 1
        props.count_y = 1

        col = self.layout.column(align=True)
        # samples of view
        col.prop(context.scene.cycles, "preview_samples")

        if context.active_object is None:
            col.label(text="No active object")
        else:
            # hide the active object
            col.prop(context.active_object, "hide_viewport")


def mesh_add_menu_draw(self, context):
    self.layout.operator('mesh.monkey_grid')


classes = [MESH_OT_monkey_grid, VIEW3D_PT_monkey_grid]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # 添加到 菜单 View3D 中的 add mesh 中
    bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # 从中移除
    bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw)


if __name__ == "__main__":
    register()
