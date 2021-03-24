# https://www.youtube.com/watch?v=xscQ9tcN4GI&list=PLa1F2ddGya_8acrgoQr1fTeIuQtkSd6BW&index=3
import bpy


# VScode: Ctrl F2 当前文件批量重命名
class MESH_OT_monkey_grid(bpy.types.Operator):
    """Let's spread some joy"""
    bl_idname = "mesh.monkey_grid"
    bl_label = "Monkey Grid"
    bl_options = {'REGISTER', 'UNDO'}

    count_x: bpy.props.IntProperty(
        name="X",
        description="Number of Monkey in the X-direction",
        default=3,
        min=1, max=10
    )
    count_y: bpy.props.IntProperty(
        name="Y",
        description="Number of Monkey in the Y-direction",
        default=4,
        min=1, max=10
    )
    size: bpy.props.FloatProperty(
        name="size",
        description="Size of Monkey",
        default=1,
        min=0, max=1
    )
    # bpy_learning\ApplicationModules\types\operator\Note.md

    @classmethod
    def poll(cls, context):
        print(f"My area is:{context.area.type}")
        # 只能在3d界面使用
        return bpy.context.area.type == 'VIEW_3D'

    def execute(self, context):

        for idx in range(self.count_x*self.count_y):
            # % fmod
            # // Floor
            # 方阵排列猴子
            x = idx % self.count_x
            y = idx // self.count_x
            bpy.ops.mesh.primitive_monkey_add(
                size=self.size, location=(x, y, 1))

        return {'FINISHED'}


classes = [MESH_OT_monkey_grid]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
